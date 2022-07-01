#!/usr/bin/env python

"""Test the `is_palindrome()` function."""


import pytest

from palindrome import is_palindrome


@pytest.mark.parametrize('is_one', [
    '',
    'a',
    'Bob',
    'Never odd or even',
    'Do geese see God?',
])
def test_is_palindrome(is_one):
    assert is_palindrome(is_one)


# noinspection SpellCheckingInspection
@pytest.mark.parametrize('is_not_one', ['abc', 'abab'])
def test_is_not_palindrome(is_not_one):
    assert not is_palindrome(is_not_one)
