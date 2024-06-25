from os import system
from .text_utils import debug
from .utils import create_file, gen_co_author, handle_conventioned_commit
from ..conventions.no_convention import just_message

def convention_flag_handler(args, debug_mode):
    convention = str(args.convention)
    debug("convention flag", convention, debug_mode)
    commit_message = ""

    if convention == "message":
        if args.message:
            commit_message = just_message(msg=args.message)
        else:
            commit_message = just_message()
        convention = "none"

    else:
        commit_message = handle_conventioned_commit(convention, args)

    create_file(convention, args.no_file)

    commit_message += gen_co_author(args.co_author)
    debug("commit message", commit_message, debug_mode)

    system(f"git commit -m '{commit_message}'")
