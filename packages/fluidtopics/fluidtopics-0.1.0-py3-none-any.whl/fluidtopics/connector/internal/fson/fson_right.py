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

from fluidtopics.connector.model.right import AccessLevel, Rights


@autovalue
class FsonRights:
    def __init__(self, access_level: AccessLevel = AccessLevel.PUBLIC,
                 groups: List[str] = None):
        self.access_level = access_level
        self.groups = groups if groups is not None else []

    @staticmethod
    def public():
        return FsonRights(AccessLevel.PUBLIC)

    @staticmethod
    def authenticated():
        return FsonRights(AccessLevel.AUTHENTICATED)

    @staticmethod
    def restricted(groups: List[str]):
        return FsonRights(AccessLevel.RESTRICTED, groups)


class RightsConverter:
    def convert_rights(self, rights: Optional[Rights]) -> Optional[FsonRights]:
        if rights is None:
            return None
        return FsonRights(rights.access_level, rights.groups)
