"""
Handler for `-s` flag.
"""
from argparse import Namespace
from pathlib import Path

from yaml import YAMLError, safe_load

from .atom import ATOM_CONVENTION_HELP
from .john_convention import JOHN_CONVENTION_HELP
from .karma_angular import karma_convention_help
from .karma_angular import ANGULAR_CONVENTION_HELP
from .symphony_cmf import SYMPHONY_CONVENTION_HELP
from .tagged import TAGGED_CONVENTION_HELP
from ..utils.colors import RESET
from ..utils.colors import MIN_ERROR
from ..utils.text_utils import debug
from ..utils.text_utils import print_help
from ..utils.utils import dump_convention

# TODO: test
def convention_help_handler(file_path: Path, args: Namespace, debug_mode: bool) -> None:
    """
    Print the help message for a convention.

    FILE_PATH is a path to a commiter config file. ARGS is a
    namespace containing the arguments pass to the
    application. If no convention is provided, and FILE_PATH
    exists, then it is opened to get the convention. If even
    that doesn't work, an error is returned.

    If DEBUG_MODE is true, debug messages are printed.
    """
    # pylint: disable=unspecified-encoding
    convention: str = ""
    if file_path.is_file() and not args.convention:
        # No convention has been provided, so we read the
        # committer.yml file for it
        debug("Found file for help", file_path, debug_mode)
        with file_path.open('rt') as target:
            try:
                config = safe_load(target)
                convention = dump_convention(config)
                debug("Convention captured", convention, debug_mode)
            except YAMLError as err:
                print(err)
    elif args.convention != "":
        # A convention was specified, so use that
        debug("Found convention in args", args, debug_mode)
        convention = args.convention
    else:
        print(f"{MIN_ERROR}No convention was specified!{RESET}")
        return

    debug("convention captured for helper", convention, debug_mode)
    get_help_to_defined_convention(convention, debug_mode)

# TODO: test
def get_help_to_defined_convention(convention: str, debug_mode: bool) -> None:
    """
    Print help for the specified convention.

    CONVENTION is the name of a predefined convention. If
    DEBUG_MODE is true, debug messages are printed.
    """
    debug("recieved convention for help catch", convention, debug_mode)
    if convention == "angular":
        print_help(ANGULAR_CONVENTION_HELP)
    elif convention == "tagged":
        print_help(TAGGED_CONVENTION_HELP)
    elif convention == "karma":
        print_help(karma_convention_help)
    elif convention == "symphony":
        print_help(SYMPHONY_CONVENTION_HELP)
    elif convention == "atom":
        print_help(ATOM_CONVENTION_HELP)
    elif convention == "john":
        print_help(JOHN_CONVENTION_HELP)
    else:
        print(f"{MIN_ERROR}The chosen convention has no helper!{RESET}")
