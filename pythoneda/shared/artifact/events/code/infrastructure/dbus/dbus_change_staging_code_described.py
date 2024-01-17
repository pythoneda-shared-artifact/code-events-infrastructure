# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact_changes/events/code/infrastructure/dbus/dbus_change_staging_code_described.py

This file defines the DbusChangeStagingCodeDescribed class.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact-changes/code-events-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from dbus_next import Message
from dbus_next.service import ServiceInterface, signal
import json
from pythoneda.shared import BaseObject
from pythoneda.shared.artifact.events.code import ChangeStagingCodeDescribed
from pythoneda.shared.artifact.events.code.infrastructure.dbus import DBUS_PATH
from pythoneda.shared.code_requests.jupyterlab import JupyterlabCodeRequest
from typing import List


class DbusChangeStagingCodeDescribed(BaseObject, ServiceInterface):
    """
    D-Bus interface for ChangeStagingCodeDescribed

    Class name: DbusChangeStagingCodeDescribed

    Responsibilities:
        - Define the d-bus interface for the ChangeStagingCodeDescribed event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusChangeStagingCodeDescribed.
        """
        super().__init__(
            "Pythoneda_Shared_Artifact_Events_Code_ChangeStagingCodeDescribed"
        )

    @signal()
    def ChangeStagingCodeDescribed(self, change: "s"):
        """
        Defines the ChangeStagingCodeDescribed d-bus signal.
        :param change: The change.
        :type change: str
        """
        pass

    @classmethod
    def path(cls) -> str:
        """
        Retrieves the d-bus path.
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH

    @classmethod
    def transform(cls, event: ChangeStagingCodeDescribed) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.artifact.events.code.ChangeStagingCodeDescribed
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.code_request.to_json(),
            event.id,
            json.dumps(event.previous_event_ids),
        ]

    @classmethod
    def sign(cls, event: ChangeStagingCodeDescribed) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.artifact.events.code.ChangeStagingCodeDescribed
        :return: The signature.
        :rtype: str
        """
        return "sss"

    @classmethod
    def parse(cls, message: Message) -> ChangeStagingCodeDescribed:
        """
        Parses given d-bus message containing a ChangeStagingCodeDescribed event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The ChangeStagingDescribed event.
        :rtype: pythoneda.shared.artifact.events.code.ChangeStagingCodeDescribed
        """
        code_request_json, event_id, prev_event_ids = message.body
        return ChangeStagingCodeDescribed(
            JupyterlabCodeRequest.from_json(code_request_json),
            None,
            event_id,
            json.loads(prev_event_ids),
        )
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
