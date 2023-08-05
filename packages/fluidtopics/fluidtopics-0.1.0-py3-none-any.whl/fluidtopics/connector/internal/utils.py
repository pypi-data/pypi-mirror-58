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

"""Contain Fluid Topics API utilities."""
import re

IETF_LANGUAGE_TAG_REGEX = re.compile(r'^[a-z]{2}(?:-[A-Z]{2})?$')


class Utils:
    """Nutshell of utils function."""

    @staticmethod
    def parse_ietf_language_tag(language_tag: str) -> str:
        lang_separator = '-'
        if language_tag is not None:
            normalized_language_tag = language_tag.replace('_', lang_separator).lower()
            if lang_separator in normalized_language_tag:
                country, region = normalized_language_tag.split(lang_separator, maxsplit=1)
                normalized_language_tag = lang_separator.join([country, region.upper()])
            if IETF_LANGUAGE_TAG_REGEX.match(normalized_language_tag):
                return normalized_language_tag

        raise ValueError('Invalid ISO code "{}".'.format(language_tag, ))

    @staticmethod
    def objects_are_equals(first, second, *order_tolerant_attributes: str):
        """Return True if @first object and @second object are equal.

        @order_tolerant_attributes is a list a iterable attributes for which the values can be unordered.
        """
        if type(first) != type(second):
            return False
        attributes = [att for att in first.__dict__.keys() if att not in order_tolerant_attributes]
        for attribute in attributes:
            if getattr(first, attribute) != getattr(second, attribute):
                return False
        for attribute in order_tolerant_attributes:
            self_attribute_values = getattr(first, attribute)
            other_attribute_values = getattr(second, attribute)
            if self_attribute_values is None or other_attribute_values is None:
                if self_attribute_values != other_attribute_values:
                    return False
            else:
                if not (all(value in other_attribute_values for value in self_attribute_values)
                        and all(value in self_attribute_values for value in other_attribute_values)):
                    return False
        return True
