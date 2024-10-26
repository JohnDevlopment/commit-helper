"""
Handler for file-based commits.

Functions:
* get_file_path()
* handle_file_based_commit()
"""
from __future__ import annotations
from os import system
from pathlib import Path

from yaml import safe_load
from yaml import YAMLError

from ..conventions.no_convention import just_message
from ..conventions.custom_convention import custom_convention
from .text_utils import debug, get_text, notify
from .utils import gen_co_author
from .utils import dump_convention
from .utils import validate_commiter_file
from .utils import handle_conventioned_commit

def handle_file_based_commit(file_path: Path, debug_mode: bool, args):
    """
    Make a commit using the convention specified in FILE_PATH.

    FILE_PATH points to a YAML config. ARGS is the Namespace
    returned from ArgumentParser.parse_args().
    """
    # pylint: disable=unspecified-encoding
    with file_path.open('rt') as stream:
        try:
            config = safe_load(stream)
            debug('convention from file', config['convention'], debug_mode)

            convention = dump_convention(config)
            if convention == 'none':
                # Because we're not using a convention, we will write just
                # an ordinary comment
                notify('You are not using a convention')
                if args.message != '':
                    commit_msg = just_message(msg=args.message)
                else:
                    commit_msg = just_message()
            elif convention == 'custom':
                # Using custom convention. We have to validate the commiter
                # file and get the tag and message from it
                notify('You are using your custom convention')
                validate_commiter_file(config)
                tag, msg = get_text()
                commit_msg = custom_convention(tag, msg, config, debug_mode)
            else:
                notify(f'You are using the {convention} convention')
                commit_msg = handle_conventioned_commit(convention, args)

            commit_msg += gen_co_author(args.co_author)
            debug('commit message', commit_msg, debug_mode)

            system(f'git commit -m "{commit_msg}"')

        except YAMLError as err:
            print(err)


def get_file_path():     # pragma: no cover
    """
    Get the path to a commiter YAML config.

    Returns either the path to commiter.yml if it exists, or
    commit-helper.yml otherwise.

    **NOTE**: There is no guarantee that the returned path
    points to an existing file.
    """
    commiter = Path('commiter.yml')
    commit_h = Path('commit-helper.yml')

    if commiter.exists():
        return commiter

    return commit_h
