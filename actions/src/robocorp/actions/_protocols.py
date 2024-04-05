import typing
from typing import Any, Callable, Sequence

from robocorp.tasks import ITask as _ITask
from robocorp.tasks import Status as _Status
from robocorp.tasks._protocols import TasksListTaskTypedDict


class IAction(_ITask, typing.Protocol):
    pass


Status = _Status

IActionCallback = Callable[[IAction], Any]
IActionsCallback = Callable[[Sequence[IAction]], Any]


class ActionsListActionTypedDict(TasksListTaskTypedDict):
    pass
