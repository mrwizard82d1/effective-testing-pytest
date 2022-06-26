#!/usr/bin/env python

"""Example of skipping a defined test."""


import pytest


@pytest.mark.skip(reason='Not yet implemented')
def test_to_be_skipped():
    pass
