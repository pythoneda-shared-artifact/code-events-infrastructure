# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/code/infrastructure/dbus/dbus_change_staging_code_execution_packaged.py

This file defines the DbusChangeStagingCodeExecutionPackaged class.

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
from dbus_next.service import signal
import json
from pythoneda.shared import Event
from pythoneda.shared.infrastructure.dbus import DbusEvent
from pythoneda.shared.artifact.events.code import ChangeStagingCodeExecutionPackaged
from pythoneda.shared.artifact.events.code.infrastructure.dbus import DBUS_PATH
from pythoneda.shared.code_requests.jupyterlab import JupyterlabCodeRequestNixFlake
from typing import List, Type


class DbusChangeStagingCodeExecutionPackaged(DbusEvent):
    """
    D-Bus interface for ChangeStagingCodeExecutionPackaged

    Class name: DbusChangeStagingCodeExecutionPackaged

    Responsibilities:
        - Define the d-bus interface for the ChangeStagingCodeExecutionPackaged event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusChangeStagingCodeExecutionPackaged.
        """
        super().__init__(
            "Pythoneda_Shared_Artifact_Events_Code_ChangeStagingCodeExecutionPackaged"
        )

    @signal()
    def ChangeStagingCodeExecutionPackaged(self, nixFlake: "s"):
        """
        Defines the ChangeStagingCodeExecutionPackaged d-bus signal.
        :param nixFlake: The Nix flake.
        :type nixFlake: str
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
    def transform(cls, event: ChangeStagingCodeExecutionPackaged) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.artifact.events.code.ChangeStagingCodeExecutionPackaged
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.nix_flake.to_json(),
            json.dumps(event.previous_event_ids),
            event.id,
        ]

    @classmethod
    def sign(cls, event: ChangeStagingCodeExecutionPackaged) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.artifact.events.code.ChangeStagingCodeExecutionPackaged
        :return: The signature.
        :rtype: str
        """
        return "sss"

    @classmethod
    def parse(cls, message: Message) -> ChangeStagingCodeExecutionPackaged:
        """
        Parses given d-bus message containing a ChangeStagingCodeExecutionPackaged event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The ChangeStagingExecutionPackaged event.
        :rtype: pythoneda.shared.artifact.events.code.ChangeStagingCodeExecutionPackaged
        """
        nix_flake_json, prev_event_ids, event_id = message.body
        return ChangeStagingCodeExecutionPackaged(
            JupyterlabCodeRequestNixFlake.from_json(nix_flake_json),
            json.loads(prev_event_ids),
            event_id,
        )

    @classmethod
    def event_class(cls) -> Type[Event]:
        """
        Retrieves the specific event class.
        :return: Such class.
        :rtype: type(pythoneda.shared.Event)
        """
        return ChangeStagingCodeExecutionPackaged


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
