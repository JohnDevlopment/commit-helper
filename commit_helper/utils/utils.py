# pylint: disable=missing-module-docstring
from __future__ import annotations
from typing import TYPE_CHECKING
import argparse
import sys

from yaml import dump

from ..conventions.atom import atom_convention
from ..conventions.john_convention import john_convention
from ..conventions.karma_angular import karma_angular_convention
from ..conventions.symphony_cmf import symphony_convention
from ..conventions.tagged import tagged_convention
from .protocols import ConfigFile
from .text_utils import handle_context_arg
from .text_utils import handle_tag_message_args
from .text_utils import notify

if TYPE_CHECKING:
    from .utils import Convention # pylint: disable=import-self
    from typing_extensions import Never

supported_conventions = [
    "angular",
    "atom",
    "john",
    "karma",
    "message",
    "symphony",
    "tagged",
]

def gen_co_author(co_author) -> str:
    """
    Generate a string denoting the commit's co-author.
    """
    return f"\nCo-authored-by: {co_author}" if co_author else ""

# TEST
def create_file(convention_name, dont_create=False):    # pragma: no cover
    """
    Create commiter.yml with the specified convention used.

    If DONT_CREATE is false (the default), then don't actually
    create the file.
    """

    if not dont_create:
        data = {
            'convention': convention_name,
        }
        # pylint: disable=unspecified-encoding
        with open('commiter.yml', 'w') as output_file:
            output_file.write(dump(data, stream=None,
                                   default_flow_style=False))
        notify('Successfully created the commiter file.')

def parser_cli():
    # pylint: disable=missing-function-docstring
    desc = "A commit formatter tool to help you follow commit conventions."
    help_convention = \
        """
        Selects a convention to be used for the commit.
        Required if there's no commiter.yml file.
        """
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-t", "--tag", dest="tag", default="",
                        help="Pass your commit tag directly")

    parser.add_argument("-m", "--message", dest="message", default="",
                        help="Pass your commit message directly")

    parser.add_argument("-ct", "--context", dest="context", default="",
                        help="Pass your commit context directly")

    parser.add_argument("-ca", "--co-author",
                        help="Make your friend an co-author to the commit",
                        dest="co_author", default="")

    parser.add_argument("-nf", "--no-file", dest="no_file",
                        help="Disables the creation of a commiter.yml file",
                        action="store_true")

    parser.add_argument("-n", "--dry-run", help="Print the commit",
                        action="store_true")

    parser.add_argument("-c", "--convention", choices=supported_conventions,
                        dest="convention", default="", help=help_convention)

    parser.add_argument("-d", "--debug", action="store_true", dest="debug",
                        help="Toggles debug option")

    parser.add_argument("-s", "--show", dest="show_convention_tags",
                        action="store_true",
                        help="Shows the rules of a given convention")

    return parser


def dump_convention(config_file: ConfigFile) -> str:
    """
    Dump the convention currently being used.

    CONFIG_FILE is a dict-like object that represents the
    commiter config file.
    """
    if config_file['convention'] is None:
        return 'none'
    return str(config_file['convention']).lower()

# this function forces the program to quit if commiter file is invalid
def validate_commiter_file(stream_file: ConfigFile):    # pragma: no cover
    """
    Validate the config file argument.

    Prints an error if STREAM_FILE does not either
    'commit_pattern' or 'context' defined.
    """
    if stream_file['commit_pattern'] is None or stream_file['context'] is None:
        print("Error: Your commiter file lacks a commit_pattern or context!")
        sys.exit(0)

def handle_conventioned_commit(convention: Convention, args: argparse.Namespace) -> str:
    """
    Dispatch the handler for the selected convention.

    CONVENTION should be one of the preset conventions, or
    "custom". If it is neither, then a normal commit message is
    returned instead.
    """
    tag, message = handle_tag_message_args(args.tag, args.message)
    commit_message: str = ""

    def _invalid_convention(_convention: Never):
        pass

    if convention in ["angular", "karma"]:
        context = handle_context_arg(args.context)
        commit_message = karma_angular_convention(tag, message, context)
    elif convention == "tagged":
        commit_message = tagged_convention(tag, message)
    elif convention == "symphony":
        commit_message = symphony_convention(tag, message)
    elif convention == "atom":
        commit_message = atom_convention(tag, message)
    elif convention == "john":
        context = handle_context_arg(args.context)
        commit_message = john_convention(tag, message, context)
    else:
        _invalid_convention(convention) # pyright: ignore[reportArgumentType]

    return commit_message
