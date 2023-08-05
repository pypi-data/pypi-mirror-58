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

from typing import List, Optional

from autovalue import autovalue
from pynject import pynject

from fluidtopics.connector.internal.fson.fson_body import FsonBody, BodyConverter
from fluidtopics.connector.internal.fson.fson_metadata import FsonMetadata, MetadataConverter
from fluidtopics.connector.model.publication import TocNode


@autovalue
class FsonSection:
    def __init__(self, id: str, title: str = None, body: FsonBody = None,
                 children: List['FsonSection'] = None,
                 metadata: List[FsonMetadata] = None, base_id: str = None,
                 variant_selector: str = None,
                 description: Optional[str] = None,
                 pretty_url: Optional[str] = None):
        self.id = id
        self.title = title
        self.body = body if body is not None else FsonBody.none()
        self.metadata = metadata if metadata is not None else []
        self.children = children if children is not None else []
        self.base_id = base_id
        self.variant_selector = variant_selector
        self.description = description
        self.pretty_url = pretty_url


@pynject
class SectionConverter:
    def __init__(self, body_converter: BodyConverter, metadata_converter: MetadataConverter):
        self._body_converter = body_converter
        self._metadata_converter = metadata_converter

    def convert_toc_node(self, node: TocNode) -> FsonSection:
        body = self._body_converter.convert_body(node.topic.body)
        section_metadata = self._metadata_converter.convert_metadata_list(node.topic.metadata)
        children = self.convert_toc(node.children)
        return FsonSection(
            node.topic.id,
            node.topic.title,
            body,
            children,
            section_metadata,
            node.topic.base_id,
            node.topic.variant_selector,
            node.topic.get_description(),
            node.topic.get_pretty_url()
        )

    def convert_toc(self, toc: Optional[List[TocNode]]) -> Optional[List[FsonSection]]:
        if toc is None:
            return None
        return [self.convert_toc_node(node) for node in toc]
