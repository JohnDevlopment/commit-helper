import pytest
import conventions.karma_angular as angular
# import conventions.changelog as changelog
# import convention.symphony_cmf as symphony
# import conventions.no_convention as no_convention


def test_angular_convention_with_context():
    message = angular.angular_convention('TAG','message','context')
 
    if not ('tag(context): message\n'):
      raise AssertionError()


def test_angular_convention_without_context():
    message = angular.angular_convention('tag','message','')

    if not ('tag: message\n'):
      raise AssertionError()


def test_changelog_convention():
    pass


def test_symphony_convention():
    pass


def test_no_convention():
    pass
