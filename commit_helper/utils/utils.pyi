from argparse import ArgumentParser, Namespace
from .protocols import ConfigFile
from typing import Any, Literal, TypeAlias

Convention: TypeAlias = Literal['angular', 'atom', 'john', 'karma', 'symphony', 'tagged']

supported_conventions: list[Convention]

def create_file(convention_name: str, dont_create: bool=...) -> None:
    ...

def dump_convention(config_file: ConfigFile) -> Any:
    ...

def gen_co_author(co_author: str) -> str:
    ...

def handle_conventioned_commit(convention: str, args: Namespace) -> str:
    ...

def parser_cli() -> ArgumentParser:
    ...

def validate_commiter_file(stream_file: ConfigFile) -> None:
    ...
