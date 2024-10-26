"""
Text utilities.

Functions:

* get_context()
"""
from .colors import RESET
from .colors import DEBUG_COLOR
from .colors import INPUT_COLOR
from .colors import NOTIFY_COLOR
from .colors import HELP

def get_context():
    """
    Query the user for the commit context.

    Returns the input in lowercase.
    """
    context = input(f"{INPUT_COLOR}type the context: {RESET}")
    return context.lower()

def get_text():
    """
    Query the user for the tag and message.

    Returns a tuple with the tag and message.
    """
    tag = input(f"{INPUT_COLOR}type the tag: {RESET}")
    msg = input(f"{INPUT_COLOR}type the commit message: {RESET}")
    return tag, msg

def handle_context_arg(context=''):
    """
    Handle the context argument.

    Prompts the user for the context if CONTEXT is empty or
    equal to `-`.
    """
    if context == "-":
        return ""
    return context if context else get_context()

def handle_tag_message_args(tag='', message=''):
    """
    Handle the tag and message arguments.

    If both TAG and MESSAGE are empty, calls `get_text()`.
    """
    return (tag, message) if f"{tag}{message}" != "" else get_text()

def sanitize_as_empty_string(string: str | None):
    """
    Sanitize the argument to always be a string.

    If STRING is None, an empty string is returned, otherwise
    STRING is returned.
    """
    return string or ""

# Print functions

def debug(message, value, show=False):
    """
    Print a message with the debug level.

    MESSAGE and VALUE are printed only if SHOW is true.
    """
    if show:
        mid = f"DEBUG: {message} ~> {value}"
        print(f"{DEBUG_COLOR}{mid}{RESET}")

def notify(message: str):
    """
    Print MESSAGE with the notify level.
    """
    print(NOTIFY_COLOR, message, RESET, sep="")

def print_help(message: str):
    """
    Print MESSAGE with the help level.
    """
    print(f"{HELP}{message}{RESET}")
