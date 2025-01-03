# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/code/infrastructure/dbus/dbus_change_staging_code_packaged.py

This file defines the DbusChangeStagingCodePackaged class.

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
from pythoneda.shared import Event, Invariants
from pythoneda.shared.infrastructure.dbus import DbusEvent
from pythoneda.shared.artifact.events.code import ChangeStagingCodePackaged
from pythoneda.shared.artifact.events.code.infrastructure.dbus import DBUS_PATH
from pythoneda.shared.code_requests.jupyterlab import JupyterlabCodeRequestNixFlake
from typing import List, Type


class DbusChangeStagingCodePackaged(DbusEvent):
    """
    D-Bus interface for ChangeStagingCodePackaged

    Class name: DbusChangeStagingCodePackaged

    Responsibilities:
        - Define the d-bus interface for the ChangeStagingCodePackaged event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusChangeStagingCodePackaged.
        """
        super().__init__(DBUS_PATH)

    @classmethod
    @property
    def name(cls) -> str:
        """
        Retrieves the d-bus interface name.
        :return: Such value.
        :rtype: str
        """
        return "Pythoneda_Shared_Artifact_Events_Code_ChangeStagingCodePackaged"

    @signal()
    def ChangeStagingCodePackaged(self, nixFlake: "s"):
        """
        Defines the ChangeStagingCodePackaged d-bus signal.
        :param nixFlake: The Nix .
        :type nixFlake: str
        """
        pass

    @classmethod
    def transform(cls, event: ChangeStagingCodePackaged) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.artifact.events.code.ChangeStagingCodePackaged
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.nix_flake.to_json(),
            json.dumps(event.previous_event_ids),
            Invariants.instance().to_json(event),
            event.id,
        ]

    @classmethod
    def sign(cls, event: ChangeStagingCodePackaged) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.artifact.events.code.ChangeStagingCodePackaged
        :return: The signature.
        :rtype: str
        """
        return "ssss"

    @classmethod
    def parse(cls, message: Message) -> ChangeStagingCodePackaged:
        """
        Parses given d-bus message containing a ChangeStagingCodePackaged event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The ChangeStagingPackaged event.
        :rtype: pythoneda.shared.artifact.events.code.ChangeStagingCodePackaged
        """
        nix_flake_json, prev_event_ids, invariants, event_id = message.body
        return (
            invariants,
            ChangeStagingCodePackaged(
                JupyterlabCodeRequestNixFlake.from_json(nix_flake_json),
                json.loads(prev_event_ids),
                event_id,
            ),
        )

    @classmethod
    def event_class(cls) -> Type[Event]:
        """
        Retrieves the specific event class.
        :return: Such class.
        :rtype: type(pythoneda.shared.Event)
        """
        return ChangeStagingCodePackaged


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
