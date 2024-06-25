from __future__ import annotations
from .protocols import ConfigFile
from .text_utils import notify
from .text_utils import handle_context_arg
from .text_utils import handle_tag_message_args
from ..conventions.atom import atom_convention
from ..conventions.karma_angular import karma_angular_convention
from ..conventions.tagged import tagged_convention
from ..conventions.symphony_cmf import symphony_convention
from typing import TYPE_CHECKING
import argparse, sys

from yaml import dump

if TYPE_CHECKING:
    from .utils import Convention
    from typing_extensions import Never

supported_conventions = [
    "angular",
    "karma",
    "tagged",
    "symphony",
    "message",
    "atom",
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
        data = dict(
            convention=convention_name
        )
        with open('commiter.yml', 'w') as output_file:
            output_file.write(dump(data, stream=None,
                                   default_flow_style=False))
        notify('Successfully created the commiter file.')

def parser_cli():
    desc = 'A commit formatter tool to help you follow commit conventions.'
    help_convention = \
        """
        Selects a convention to be used for the commit.
        Required if there's no commiter.yml file.
        """
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-t', '--tag', dest='tag', default='',
                        help='Pass your commit tag directly')

    parser.add_argument('-m', '--message', dest='message', default='',
                        help='Pass your commit message directly')

    parser.add_argument('-ct', '--context', dest='context', default='',
                        help='Pass your commit context directly')

    parser.add_argument('-ca', '--co-author',
                        help='Make your friend an co-author to the commit',
                        dest='co_author', default='')

    parser.add_argument('-nf', '--no-file', dest='no_file',
                        help='Disables the creation of a commiter.yml file',
                        action='store_true')

    parser.add_argument('-c', '--convention', choices=supported_conventions,
                        dest='convention', default='', help=help_convention)

    parser.add_argument('-d', '--debug', action='store_true', dest='debug',
                        help='Toggles debug option')

    parser.add_argument('-s', '--show', dest='show_convention_tags',
                        default='False', action='store_true',
                        help='Shows the rules of a given convention')

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

    def _invalid_convention(convention: Never):
        pass

    if convention == "angular" or convention == "karma":
        context = handle_context_arg(args.context)
        commit_message = karma_angular_convention(tag, message, context)
    elif convention == "tagged":
        commit_message = tagged_convention(tag, message)
    elif convention == "symphony":
        commit_message = symphony_convention(tag, message)
    elif convention == "atom":
        commit_message = atom_convention(tag, message)
    else:
        _invalid_convention(convention)

    return commit_message
