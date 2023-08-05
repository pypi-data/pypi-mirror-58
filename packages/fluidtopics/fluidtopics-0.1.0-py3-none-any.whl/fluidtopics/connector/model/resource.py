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

from typing import Optional

from autovalue import autovalue


@autovalue
class Resource:
    """Resource of a Publication.

    Consider using ResourceBuilder to create a Resource."""
    def __init__(self, id: str, content: Optional[bytes], filename: str, mime_type: Optional[str] = None,
                 indexable_content: str = None, url: str = None):
        """Prefer using ResourceBuilder to create a Resource.

        :param id: ID of the Resource. It should be unique for the upload source.
        :param content: Binary content. Not mandatory if you specify an url.
        :param filename: Name used when the resource is downloaded.
        :param mime_type: MIME type of the Resource. Guessed from the content if not set.
        :param indexable_content: If the Resource is an UD content,
                                  indexable_content is indexed as the content
                                  of the UD.
        :param url: If the Resource is a map attachment, this parameter is used
                    to create an URL attachment."""
        self.id = id
        self.content = content
        self.filename = filename
        self.mime_type = mime_type
        self.indexable_content = indexable_content
        self.url = url


class InvalidResource(Exception):
    pass


class ResourceBuilder:
    """Helper to create a valid Resource."""
    def __init__(self, resource: Resource = None):
        """Create a ResourceBuilder.

        :param resource: Built Resource will have same fields than
                         resource except if you update them."""
        self._id = resource.id if resource else None
        self._content = resource.content if resource else None
        self._filename = resource.filename if resource else None
        self._mime_type = resource.mime_type if resource else None
        self._indexable_content = resource.indexable_content if resource else None
        self._url = resource.url if resource else None

    def resource_id(self, id: Optional[str]) -> 'ResourceBuilder':
        """Set the ID of the Resource. It should be unique for a given source."""
        self._id = id
        return self

    def content(self, content: Optional[bytes]) -> 'ResourceBuilder':
        """Set binary content. Not mandatory if you specify an url."""
        self._content = content
        return self

    def filename(self, filename: Optional[str]) -> 'ResourceBuilder':
        """Name used when the resource is downloaded."""
        self._filename = filename
        return self

    def mime_type(self, mime_type: Optional[str]) -> 'ResourceBuilder':
        """MIME type of the Resource. Guessed from the content if not set."""
        self._mime_type = mime_type
        return self

    def indexable_content(self, indexable_content: Optional[str]) -> 'ResourceBuilder':
        """If the Resource is an UD content, indexable_content is indexed as the content of the UD."""
        self._indexable_content = indexable_content
        return self

    def url(self, url: Optional[str]) -> 'ResourceBuilder':
        """If the Resource is a map attachment, this parameter is used to create an URL attachment."""
        self._url = url
        return self

    def build(self) -> Resource:
        """Build the Resource from information specified before.

        ID and filename are mandatory. Content or URL should be specified.
        :raises:
            InvalidResource: One of the requirement is not fulfilled."""
        if not self._id:
            raise InvalidResource('Resource should have an id')
        if not self._filename:
            raise InvalidResource('Resource {} should have a filename'.format(self._id))
        if self._content is None and not self._url:
            raise InvalidResource('Resource {} should have a content or an url'.format(self._id))
        return Resource(self._id, self._content, self._filename, self._mime_type, self._indexable_content, self._url)
