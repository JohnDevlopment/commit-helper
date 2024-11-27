"""
Text utilities.

Functions:

* get_context()
* get_text()
* handle_context_arg()
* handle_tag_message_args()
* sanitize_as_empty_string()
* debug()
* notify()
* print_help()
"""
from pathlib import Path
import atexit
import readline

from .colors import RESET
from .colors import DEBUG_COLOR
from .colors import INPUT_COLOR
from .colors import NOTIFY_COLOR
from .colors import HELP

_Init = False

@atexit.register
def _cleanup() -> None:
    hf = Path("/tmp/.commit-history")
    if hf.exists():
        readline.append_history_file(5, hf)
    else:
        readline.write_history_file(hf)

def _init() -> None:
    global _Init
    if not _Init:
        _Init = True
        hf = Path("/tmp/.commit-history")
        if hf.exists():
            readline.read_history_file(hf)

def get_context() -> str:
    """
    Query the user for the commit context.

    Returns the input in lowercase.
    """
    context = input(f"{INPUT_COLOR}type the context: {RESET}")
    return context.lower()

def get_text() -> tuple[str, str]:
    """
    Query the user for the tag and message.

    Returns a tuple with the tag and message.
    """
    tag = input(f"{INPUT_COLOR}type the tag: {RESET}")
    msg = input(f"{INPUT_COLOR}type the commit message: {RESET}")
    return tag, msg

def handle_context_arg(context: str="") -> str:
    """
    Handle the context argument.

    Prompts the user for the context if CONTEXT is empty or
    equal to `-`.
    """
    if context == "-":
        return ""
    return context if context else get_context()

def handle_tag_message_args(tag='', message='') -> tuple[str, str]:
    """
    Handle the tag and message arguments.

    If both TAG and MESSAGE are empty, calls `get_text()`.
    """
    return (tag, message) if f"{tag}{message}" != "" else get_text()

def sanitize_as_empty_string(string: str | None) -> str:
    """
    Sanitize the argument to always be a string.

    If STRING is None, an empty string is returned, otherwise
    STRING is returned.
    """
    return string or ""

# Print functions

def debug(message, value, show=False) -> None:
    """
    Print a message with the debug level.

    MESSAGE and VALUE are printed only if SHOW is true.
    """
    if show:
        mid = f"DEBUG: {message} ~> {value}"
        print(f"{DEBUG_COLOR}{mid}{RESET}")

def notify(message: str) -> None:
    """
    Print MESSAGE with the notify level.
    """
    print(NOTIFY_COLOR, message, RESET, sep="")

def print_help(message: str) -> None:
    """
    Print MESSAGE with the help level.
    """
    print(f"{HELP}{message}{RESET}")

_init()
