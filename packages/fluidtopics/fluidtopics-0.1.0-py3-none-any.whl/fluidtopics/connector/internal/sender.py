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

import logging

import requests
from requests import Response

logger = logging.getLogger(__name__)


class RemoteSender:
    def __init__(self, url: str, auth: str, source_id: str):
        self.url = url
        self.auth = auth
        self.source_id = source_id

    def send(self, data: bytes, filename: str) -> Response:
        logger.debug('Sending %s to %s...', filename, self.url)
        headers = {'Authorization': 'Basic {}'.format(self.auth)}
        response = requests.post(self._upload_endpoint(), files={filename: data}, headers=headers)
        if response.status_code != 200:
            msg = 'Error while sending %s to %s : %s : %s'
            logger.error(msg, filename, self.url, response.status_code, response.content)
        return response

    def _upload_endpoint(self) -> str:
        return '{}/api/admin/khub/sources/{}/upload'.format(self.url, self.source_id)
