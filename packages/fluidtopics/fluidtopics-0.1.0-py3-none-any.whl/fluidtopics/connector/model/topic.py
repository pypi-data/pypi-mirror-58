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
from deprecated.sphinx import deprecated

from fluidtopics.connector.internal.utils import Utils
from fluidtopics.connector.model.body import Body
from fluidtopics.connector.model.metadata import Metadata, SemanticMetadata


@autovalue
class Topic:
    """A Topic is an element which compose the table of content of a Publication."""

    def __init__(self, id: str, title: str = None, body: Body = None,
                 metadata: List[Metadata] = None, base_id: str = None,
                 variant_selector: str = None, description: Optional[str] = None,
                 pretty_url: Optional[str] = None):
        """Prefer using TopicBuilder to build a Topic.

        :param id: Origin ID of the Topic. It should be unique for a given source.
        :param title: Title of the Topic. Can be None when a {title} metadata is specified
        :param body: Content of the Topic.
        :param metadata: List of Metadata.
        :param base_id: Topics with the same base_id are clustered in search page and cross-book links.
                        Fallback to id if None. Can be override by {cluster_id} metadata for search page clustering.
        :param variant_selector: Deprecated (it's here for compatibility but no longer used. Put None)
        :param description: Description displayed in search page. Set {description} metadata.
        :param pretty_url: Pretty name used to build a pretty URL. Set {pretty_url} metadata.""".format(
            title=SemanticMetadata.TITLE,
            cluster_id=SemanticMetadata.CLUSTER_ID,
            description=SemanticMetadata.DESCRIPTION,
            pretty_url=SemanticMetadata.PRETTY_URL)
        self.id = id
        self.title = title
        self.metadata = metadata if metadata is not None else []
        self.body = body if body is not None else Body.none()
        self.base_id = base_id
        self.variant_selector = variant_selector
        self.description = description
        self.pretty_url = pretty_url

    def __eq__(self, other):
        """Return self==other."""
        return Utils.objects_are_equals(self, other, 'metadata')

    def get_title(self) -> str:
        """Helper to get title. Prefer using it than title field which can be empty."""
        meta_title = self._get_metadata(SemanticMetadata.TITLE)
        return meta_title.first_value if meta_title is not None else self.title

    def get_description(self) -> str:
        """Helper to get description. Prefer using it than description field."""
        meta_description = self._get_metadata(SemanticMetadata.DESCRIPTION)
        return meta_description.first_value if meta_description is not None else self.description

    def get_pretty_url(self) -> str:
        """Helper to get description. Prefer using it than pretty_url field."""
        meta_pretty_url = self._get_metadata(SemanticMetadata.PRETTY_URL)
        return meta_pretty_url.first_value if meta_pretty_url is not None else self.pretty_url

    def _get_metadata(self, key: str) -> Optional[Metadata]:
        meta = self.metadata if self.metadata is not None else []
        return next((m for m in meta if m.key == key), None)


class InvalidTopic(Exception):
    pass


class TopicBuilder:
    """Helper to create a valid Topic."""

    def __init__(self, topic: Topic = None):
        """Create a TopicBuilder.

        :param topic: Built Topic will have same fields than
                            topic except if you update them."""

        self._id = topic.id if topic else None
        self._title = topic.title if topic else None
        self._body = topic.body if topic else None
        self._metadata = topic.metadata if topic else []
        self._base_id = topic.base_id if topic else None
        self._variant_selector = topic.variant_selector if topic else None
        self._description = topic.description if topic else None
        self._pretty_url = topic.pretty_url if topic else None

    def id(self, topic_id: str) -> 'TopicBuilder':
        """Set the ID of the Topic. It should be unique for a given source."""
        self._id = topic_id
        return self

    def title(self, title) -> 'TopicBuilder':
        """Set the title of the Topic."""
        self._title = title
        return self

    def body(self, body: Body) -> 'TopicBuilder':
        """Set the Body of the Topic."""
        self._body = body
        return self

    def metadata(self, metadata: List[Metadata]) -> 'TopicBuilder':
        """Set metadata list of the Topic."""
        self._metadata = metadata
        return self

    def base_id(self, base_id: str) -> 'TopicBuilder':
        """Set the base ID of the Topic.

        Topics with the same base_id are clustered in search page and cross-book links.
        Fallback to id if None. Can be override by {cluster_id} metadata for search page clustering
        """.format(cluster_id=SemanticMetadata.CLUSTER_ID)
        self._base_id = base_id
        return self

    @deprecated(reason='Variant selector value is ignored.But this method is kept for compatibility.')
    def variant_selector(self, variant_selector: str) -> 'TopicBuilder':
        self._variant_selector = variant_selector
        return self

    def description(self, description: str) -> 'TopicBuilder':
        """Set the description which is displayed in search page."""
        self._description = description
        return self

    def pretty_url(self, pretty_url: str) -> 'TopicBuilder':
        """Set the pretty name which is used to build a pretty URL."""
        self._pretty_url = pretty_url
        return self

    def build(self) -> Topic:
        """Build the Topic from information specified before.

        ID and title are mandatory.
        :raises:
            InvalidTopic: One of the requirement is not fulfilled."""
        if not self._id:
            raise InvalidTopic('Missing ID when building topic')
        if self._title:
            metadata_title = Metadata.title(self._title)
            self._metadata.append(metadata_title)
        return Topic(self._id, None, self._body, self._metadata, self._base_id, self._variant_selector,
                     self._description, self._pretty_url)
