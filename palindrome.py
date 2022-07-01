#!/usr/bin/env python

"""Module for working with palindromes."""
import string


def is_palindrome(to_test):
    to_test_reversed = list(to_test)
    to_test_reversed.reverse()
    against = ''.join(to_test_reversed)

    def strip_punctuation(s):
        translation_table = str.maketrans({c: None for c in string.punctuation})
        return s.translate(translation_table)

    def canonicalize(s):
        return strip_punctuation(s.lower().replace(' ', ''))

    return canonicalize(to_test) == canonicalize(against)
