#!/usr/bin/env python

"""Tests formatting data for display."""


import pytest



from format_data import (
    format_data_for_display,
    format_data_for_excel,
)


@pytest.fixture
def example_people_data():
    people = [
        {
            'given_name': 'Alfonso',
            'family_name': 'Ruiz',
            'title': 'Senior Software Engineer',
        },
        {
            'given_name': 'Sayid',
            'family_name': 'Khan',
            'title': 'Project Manager',
        },
    ]
    return people



def test_format_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        'Alfonso Ruiz: Senior Software Engineer',
        'Sayid Khan: Project Manager',
    ]




def test_format_for_excel(example_people_data):
    expect = '\n'.join(['given,family,title',
                        'Alfonso,Ruiz,"Senior Software Engineer"',
                        'Sayid,Khan,"Project Manager"'])
    assert format_data_for_excel(example_people_data) == expect
