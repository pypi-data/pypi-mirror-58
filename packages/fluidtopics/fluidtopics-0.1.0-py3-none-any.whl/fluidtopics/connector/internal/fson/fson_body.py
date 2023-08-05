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

from autovalue import autovalue

from fluidtopics.connector.model.body import Body


@autovalue
class FsonBody:
    def __init__(self, html: str = None, resource_reference: str = None):
        self.html = html
        self.resource_reference = resource_reference

    @staticmethod
    def none() -> 'FsonBody':
        return FsonBody()

    @staticmethod
    def html_body(html_body: str) -> 'FsonBody':
        return FsonBody(html=html_body)

    @staticmethod
    def file(resource_reference: str) -> 'FsonBody':
        return FsonBody(resource_reference=resource_reference)


class BodyConverter:
    def convert_body(self, body: Body) -> FsonBody:
        return FsonBody(body.html, body.resource_reference)
