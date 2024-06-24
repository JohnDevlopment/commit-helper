# pylint: disable=missing-module-docstring
from __future__ import annotations
from .utils.utils import parser_cli
from .utils.text_utils import debug
from .utils.file_handler import handle_file_based_commit
from .utils.file_handler import get_file_path
from .utils.flag_commit_handler import convention_flag_handler
from .conventions.convention_help_handler import convention_help_handler

def main():
    # pylint: disable=missing-function-docstring
    parser = parser_cli()
    args = parser.parse_args()

    debug_mode: bool = args.debug
    debug('args variable', args, debug_mode)

    file_path = get_file_path()
    debug('file_path', file_path, debug_mode)

    # This argument is a bool; it indicates whether to show
    # the rules of the selected convention
    if args.show_convention_tags:
        convention_help_handler(file_path, args, debug_mode)
        return

    # The CONVENTION argument was provided, so we write a
    # message using that convention
    if args.convention:
        convention_flag_handler(args, debug_mode)
        return

    # No convention was provided, so we try to read a file
    if file_path.is_file():
        handle_file_based_commit(file_path, debug_mode, args)
        return

    debug('parser full return', parser.parse_args(), debug_mode)
    parser.print_help()
