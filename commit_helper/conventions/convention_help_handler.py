# dependencies imports
from .atom import atom_convention_help
from .karma_angular import karma_convention_help
from .karma_angular import angular_convention_help
from .symphony_cmf import symphony_convention_help
from .tagged import tagged_convention_help
from ..utils.colors import HELP
from ..utils.colors import RESET
from ..utils.colors import MIN_ERROR
from ..utils.text_utils import debug
from ..utils.text_utils import print_help
from ..utils.utils import dump_convention
from argparse import Namespace
from pathlib import Path

from yaml import YAMLError, safe_load

# TODO: test
def convention_help_handler(file_path: Path, args: Namespace, debug_mode: bool) -> None:
    convention: str = ""
    if file_path.is_file() and not args.convention:
        debug('Found file for help', str(file_path), debug_mode)
        with open(str(file_path)) as target:
            try:
                config = safe_load(target)
                convention = dump_convention(config)
                debug('Convention captured', convention, debug_mode)
            except YAMLError as err:
                print(err)
    elif args.convention is not '':
        debug('Found convention in args', args, debug_mode)
        convention = args.convention
    else:
        print(f"{MIN_ERROR}No convention was specified!{RESET}")
        return

    debug('convention captured for helper', convention, debug_mode)
    get_help_to_defined_convention(convention, debug_mode)

# TODO: test
def get_help_to_defined_convention(convention: str, debug_mode: bool) -> None:
    debug('recieved convention for help catch', convention, debug_mode)
    if convention == 'angular':
        print_help(angular_convention_help)

    elif convention == 'tagged':
        print_help(tagged_convention_help)

    elif convention == 'karma':
        print_help(karma_convention_help)

    elif convention == 'symphony':
        print_help(symphony_convention_help)

    elif convention == 'atom':
        print_help(atom_convention_help)

    else:
        print(MIN_ERROR + 'The chosen convention has no helper!' + RESET)
