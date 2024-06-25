# pylint: disable=missing-module-docstring
import builtins

from pytest import MonkeyPatch
import yaml

from commit_helper.conventions import (
    atom,
    custom_convention as custom,
    john_convention as john,
    karma_angular as angular,
    symphony_cmf as symphony,
    no_convention,
    tagged
)

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

class TestNoConvention:
    def test_no_convention_without_args(self, monkeypatch: MonkeyPatch):
        inputs = ["message"]

        def mock_input(_s):
            return inputs.pop(0)
        # monkeypatch.setattr("commit_helper.conventions.no_convention.input", mock_input)
        monkeypatch.setattr(builtins, "input", mock_input)

        message = no_convention.just_message()
        assert message == "Message\n"

    def test_no_convention_with_args(self):
        message = no_convention.just_message("Message")
        assert message == "Message\n"

class TestJohnConvention:
    def test_with_args(self):
        message = john.john_convention("tag", "message", "context")
        assert message == "[TAG] Context: message"

    def test_with_args_but_no_context(self):
        message = john.john_convention("tag", "message", "")
        assert message == "[TAG] message"

class TestKarmaAngularConvention:
    def test_with_context(self):
        message = angular.karma_angular_convention('TAG', 'message', 'context')
        assert message == 'tag(context): message\n'

    def test_karma_angular_convention_without_context(self):
        message = angular.karma_angular_convention("tag", "message", "")
        assert message == "tag: message\n"

def test_tagged_convention():
    message = tagged.tagged_convention("tag", "message")
    assert message == "TAG: message\n"

def test_symphony_convention():
    message = symphony.symphony_convention("tag", "message")
    assert message == "[Tag] message\n"

def test_custom_convention():
    fyle = yaml.safe_load("""
    convention: custom
    commit_pattern: tag..:..message
    context: false
    """)

    msg = "a nice function"
    tag = "add"
    message = custom.custom_convention(tag, msg, fyle, True)
    assert message == "add..:..a nice function\n"

def test_atom_convention():
    message = atom.atom_convention("CaNary", "STUFF")
    assert message == ":canary: Stuff\n"
