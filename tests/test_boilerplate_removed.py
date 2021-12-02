"""
This file checks that all the example boilerplate text has been removed.
It can be deleted when all the contained tests pass
"""
import os

import pytest


@pytest.fixture
def setupcfg():
    import configparser

    conf = configparser.ConfigParser()
    conf.read("setup.cfg")

    return conf["metadata"]


# setup.cfg
def test_module_description(setupcfg):
    if "One line description of your module" in setupcfg["description"]:
        raise AssertionError(
            "Please change description in ./setup.cfg "
            "to be a one line description of your module"
        )


def assert_not_contains_text(path, text, explanation):
    if os.path.exists(path):
        with open(path, "r") as f:
            contents = f.read().replace("\n", " ")
        if text in contents:
            raise AssertionError(f"Please change ./{path} {explanation}")


def assert_not_exists(path, explanation):
    if os.path.exists(path):
        raise AssertionError(f"Please delete ./{path} {explanation}")


# README
def test_changed_README():
    assert_not_contains_text(
        "README.rst",
        "This is where you should write a short paragraph",
        "to include a paragraph on what your module does",
    )


# README
def test_changed_CHANGELOG():
    assert_not_contains_text(
        "CHANGELOG.rst",
        "When you make a change, put it here",
        "To summarize changes to your module as you make them",
    )
