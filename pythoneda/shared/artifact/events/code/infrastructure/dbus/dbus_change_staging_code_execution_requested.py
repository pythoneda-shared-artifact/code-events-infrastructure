# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/code/infrastructure/dbus/dbus_change_staging_code_execution_requested.py

This file defines the DbusChangeStagingCodeExecutionRequested class.

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
from pythoneda.shared.code_requests.jupyterlab import JupyterlabCodeRequest
from pythoneda.shared.artifact.events.code import ChangeStagingCodeExecutionRequested
from pythoneda.shared.artifact.events.code.infrastructure.dbus import DBUS_PATH
from typing import List, Type


class DbusChangeStagingCodeExecutionRequested(DbusEvent):
    """
    D-Bus interface for ChangeStagingCodeExecutionRequested

    Class name: DbusChangeStagingCodeExecutionRequested

    Responsibilities:
        - Define the d-bus interface for the ChangeStagingCodeExecutionRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusChangeStagingCodeExecutionRequested.
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
        return (
            "Pythoneda_Shared_Artifact_Events_Code_ChangeStagingCodeExecutionRequested"
        )

    @signal()
    def ChangeStagingCodeExecutionRequested(self, codeRequest: "s"):
        """
        Defines the ChangeStagingCodeExecutionRequested d-bus signal.
        :param codeRequest: The code request.
        :type codeRequest: str
        """
        pass

    @classmethod
    def transform(cls, event: ChangeStagingCodeExecutionRequested) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.artifact.events.code.ChangeStagingCodeExecutionRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.code_request.to_json(),
            json.dumps(event.previous_event_ids),
            Invariants.instance().to_json(event),
            event.id,
        ]

    @classmethod
    def sign(cls, event: ChangeStagingCodeExecutionRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.artifact.events.code.ChangeStagingCodeExecutionRequested
        :return: The signature.
        :rtype: str
        """
        return "ssss"

    @classmethod
    def parse(cls, message: Message) -> ChangeStagingCodeExecutionRequested:
        """
        Parses given d-bus message containing a ChangeStagingCodeExecutionRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The ChangeStagingExecutionRequested event.
        :rtype: pythoneda.shared.artifact.events.code.ChangeStagingCodeExecutionRequested
        """
        code_request_json, prev_event_ids, invariants, event_id = message.body
        return (
            invariants,
            ChangeStagingCodeExecutionRequested(
                JupyterlabCodeRequest.from_json(code_request_json),
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
        return ChangeStagingCodeExecutionRequested


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
