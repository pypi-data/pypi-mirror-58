"""Container classes and enums.

.. module:: containers
    :synopsis: Container classes and enums.

.. moduleauthor:: Simon Larsén
"""
import collections
import enum
import argparse
import pluggy

from typing import Mapping, Any, Optional, Callable, Iterable

from repobee_plug import _exceptions


hookspec = pluggy.HookspecMarker(__package__)
hookimpl = pluggy.HookimplMarker(__package__)


class Status(enum.Enum):
    """Status codes enum."""

    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"


class HookResult(
    collections.namedtuple("HookResult", ("hook", "status", "msg", "data"))
):
    """Container for storing results from hooks."""

    def __new__(
        cls,
        hook: str,
        status: Status,
        msg: str,
        data: Mapping[Any, Any] = None,
    ):
        """
        Args:
            hook: Name of the hook.
            status: Status of the hook execution.
            msg: A hook message.
            data: Any additional data that the hook would like to report. This
                is primarily for storing hook results as JSON.
        """
        return super().__new__(cls, hook, status, msg, data)


class ExtensionParser(argparse.ArgumentParser):
    """An ArgumentParser specialized for RepoBee extension commands."""

    def __init__(self):
        super().__init__(add_help=False)


class BaseParser(enum.Enum):
    """Enumeration of base parsers that an extension command can request."""

    BASE = "base"
    STUDENTS = "students"
    REPO_NAMES = "repo-names"
    MASTER_ORG = "master-org"


class ExtensionCommand(
    collections.namedtuple(
        "ExtensionCommand",
        (
            "parser",
            "name",
            "help",
            "description",
            "callback",
            "requires_api",
            "requires_base_parsers",
        ),
    )
):
    """Class defining an extension command for the RepoBee CLI."""

    def __new__(
        cls,
        parser: ExtensionParser,
        name: str,
        help: str,
        description: str,
        callback: Callable[[argparse.Namespace, "apimeta.API"], None],
        requires_api: bool = False,
        requires_base_parsers: Optional[Iterable[BaseParser]] = None,
    ):
        """
        Args:
            parser: The parser to use for the CLI.
            name: Name of the command.
            help: Text that will be displayed when running ``repobee -h``
            description: Text that will be displayed when calling the ``-h``
                option for this specific command. Should be elaborate in
                describing the usage of the command.
            callback: A callback function that is called if this command is
                used on the CLI. It is passed the parsed namespace and the
                platform API, and is expected to return nothing.
            requires_api: If True, the base arguments required for the platform
                API are added as options to the extension command, and the
                platform API is then passed to the callback function. It is
                then important not to have clashing option names. If False, the
                base arguments are not added to the CLI, and None is passed in
                place of the API.
        """
        if not isinstance(parser, ExtensionParser):
            raise _exceptions.ExtensionCommandError(
                "parser must be a {.__name__}".format(ExtensionParser)
            )
        if not callable(callback):
            raise _exceptions.ExtensionCommandError(
                "callback must be a callable"
            )
        return super().__new__(
            cls,
            parser,
            name,
            help,
            description,
            callback,
            requires_api,
            requires_base_parsers,
        )

    def __eq__(self, other):
        """Two ExtensionCommands are equal if they compare equal in all
        respects except for the parser, as argpars.ArgumentParser instances do
        not implement __eq__.
        """
        _, *rest = self
        _, *other_rest = other
        return rest == other_rest


ReviewAllocation = collections.namedtuple(
    "ReviewAllocation", "review_team reviewed_team"
)

Review = collections.namedtuple("Review", ["repo", "done"])

Deprecation = collections.namedtuple(
    "Deprecation", ["replacement", "remove_by_version"]
)
