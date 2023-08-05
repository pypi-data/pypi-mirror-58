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

from fluidtopics.connector.model.resource import Resource


@autovalue
class FsonResource:
    def __init__(self, id: str, filename: str = None,
                 mime_type: str = None, description: str = None,
                 indexable_content: str = None, url: str = None):
        self.id = id
        self.filename = filename
        self.mime_type = mime_type
        self.description = description
        self.indexable_content = indexable_content
        self.url = url


class ResourceConverter:
    def convert_resource(self, resource: Resource, description: Optional[str] = None) -> FsonResource:
        return FsonResource(
            resource.id,
            resource.filename,
            resource.mime_type,
            description,
            resource.indexable_content,
            resource.url
        )
