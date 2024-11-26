"""
Handle the -c option.
"""
from __future__ import annotations
from os import system
from typing import TYPE_CHECKING

from ..conventions.no_convention import just_message
from .text_utils import debug
from .utils import create_file, gen_co_author, handle_conventioned_commit

if TYPE_CHECKING:
    from argparse import Namespace

def convention_flag_handler(args: Namespace, debug_mode: bool):
    """
    Handle the convention option.

    If the the convention is `message`, then a message-only
    commit is created, otherwise the given convention is used to
    create the commit.
    """
    convention = str(args.convention)
    debug("convention flag", convention, debug_mode)
    commit_message = ""

    if convention == "message":
        # Only a message
        if args.message:
            commit_message = just_message(msg=args.message)
        else:
            commit_message = just_message()
        convention = "none"
    else:
        # Commit with a convention
        commit_message = handle_conventioned_commit(convention, args)

    create_file(convention, args.no_file)

    commit_message += gen_co_author(args.co_author)
    debug("commit message", commit_message, debug_mode)

    if args.dry_run:
        print(f"git commit -m '{commit_message}'")
    else:
        system(f"git commit -m '{commit_message}'")
