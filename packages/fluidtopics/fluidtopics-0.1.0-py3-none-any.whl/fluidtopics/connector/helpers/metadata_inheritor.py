# Copyright 2019 Antidot opensource@antidot.net
#
# This file is part of Fluid-Topics python API
#
# Fluid-Topics python API is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation; either version 2 of
# the License, or (at your option) any later version.
#
# Fluid-Topics python API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from typing import List, Dict

from fluidtopics.connector.model.metadata import SemanticMetadata, MetadataType, Metadata
from fluidtopics.connector.model.publication import Publication, UnstructuredContent, TocNode, PublicationBuilder, \
    StructuredContent
from fluidtopics.connector.model.topic import TopicBuilder

PRODUCER = 'Normalizer'
INHERIT_MESSAGE = 'Inherited from parent metadata'
ENRICH_MESSAGE = 'Enriched from parent metadata'


class MetadataInheritor:
    """Helper to inherit metadata in Publications.

    Book (book_meta)
    | - Topic (topic_meta)
        | - Sub topic (sub_topic_meta)

    will become

    Book (book_meta)
    | - Topic (topic_meta, book_meta)
        | - Sub topic (sub_topic_meta, topic_meta, book_meta)

    By default, SemanticMetadata are not inherited."""

    def __init__(self, ignored_keys: List[str] = None):
        """Create a MetadataInheritor.

        :param ignored_keys: keys of metadata that should not be inherited."""
        ignored_keys = ignored_keys or []
        self.ignored_keys = {*ignored_keys, *SemanticMetadata.values}

    def inherit_metadata(self, publication: Publication) -> Publication:
        """Inherit metadata in the Publication.
        If a topic inherit a metadata it already have, values are merged.
        For example:

        {key = value1} inherit from {key = value2} => {key = [value1, value2]}

        This method do nothing if publication is an UD.
        :raises:
            KeyError: Publication or a Topic have two metadata with the same key."""
        if isinstance(publication.content, UnstructuredContent):
            return publication
        metadata = self._build_metadata_dict(publication.metadata or [])
        metadata = self._filter_ignored_metadata(metadata)
        content = self._inherit_metadata_for_content(publication.content, metadata)
        return PublicationBuilder(publication) \
            .content(content) \
            .build()

    def _build_metadata_dict(self, metadata: List[Metadata]) -> Dict[str, Metadata]:
        metadata_dict = {}
        for m in metadata:
            if m.key in metadata_dict:
                raise KeyError('Multiple metadata with the same key are forbidden. Contains {} and {}'
                               .format(m, metadata_dict[m.key]))
            metadata_dict[m.key] = m
        return metadata_dict

    def _filter_ignored_metadata(self, metadata: Dict[str, Metadata]) -> Dict[str, Metadata]:
        return {k: m for k, m in metadata.items() if k not in self.ignored_keys}

    def _inherit_metadata_for_content(self, content: StructuredContent,
                                      metadata: Dict[str, Metadata]) -> StructuredContent:
        toc_nodes = self._inherit_metadata_for_nodes(content.toc, metadata)
        return StructuredContent(toc_nodes, content.editorial_type)

    def _inherit_metadata_for_nodes(self, toc_nodes: List[TocNode], metadata: Dict[str, Metadata]) -> List[TocNode]:
        return [self._inherit_metadata_for_node(n, metadata) for n in toc_nodes]

    def _inherit_metadata_for_node(self, toc_node: TocNode, metadata: Dict[str, Metadata]) -> TocNode:
        topic_metadata = self._build_metadata_dict(toc_node.topic.metadata)
        merged_metadata = self._merge_metadata(topic_metadata, metadata)
        topic = TopicBuilder(toc_node.topic) \
            .metadata(list(merged_metadata.values())) \
            .build()
        metadata_to_transmit = self._filter_ignored_metadata(merged_metadata)
        children = self._inherit_metadata_for_nodes(toc_node.children, metadata_to_transmit)
        return TocNode(topic, children)

    def _merge_metadata(self, metadata: Dict[str, Metadata], to_merge: Dict[str, Metadata]) -> Dict[str, Metadata]:
        merged_metadata = dict(**metadata)
        for key, meta in to_merge.items():
            if key in merged_metadata:
                merged_metadata[key] = self._merge_meta(merged_metadata[key], meta)
            else:
                merged_metadata[key] = Metadata(meta.type, meta.key, meta.values, PRODUCER, INHERIT_MESSAGE)
        return merged_metadata

    def _merge_meta(self, old_meta: Metadata, new_meta: Metadata) -> Metadata:
        values = old_meta.values.union(new_meta.values)
        if values != old_meta.values:
            meta_type = old_meta.type if old_meta.type == new_meta.type else MetadataType.STRING_TREE
            merged_meta = Metadata(meta_type, old_meta.key, values, PRODUCER, ENRICH_MESSAGE)
            return old_meta.update(merged_meta)
        return old_meta
