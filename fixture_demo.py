#!/usr/bin/env python

"""Demonstrate `pytest` fixtures."""


import pytest


@pytest.fixture
def example_fixture():
    return 1


def test_with_fixture(example_fixture):
    assert example_fixture == 1
