"""
Custom commit convention.

Custom commits are only acceptable when you have a config
file.
"""
from ..utils.text_utils import get_context, debug

def custom_convention(tag, message, config_file, debug_mode):
    # pylint: disable=missing-function-docstring
    debug('tag', tag, debug_mode)
    debug('message', message, debug_mode)
    debug('pattern from file', config_file['commit_pattern'], debug_mode)

    pattern = str(config_file['commit_pattern'] or '')
    debug('pattern acquired', pattern, debug_mode)

    context = ''
    pattern = pattern.replace('tag', str(tag))
    pattern = pattern.replace('message', str(message))

    if config_file['context']:
        context = get_context()
        pattern = pattern.replace('context', context)

    debug('pattern post replace', pattern, debug_mode)
    pattern += '\n'
    return pattern
