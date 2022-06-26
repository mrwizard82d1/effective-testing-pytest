#!/usr/bin/env python

"""Tests formatting data for display."""



from format_data import format_data_for_display



def test_format_for_display():
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

    assert format_data_for_display(people) == [
        'Alfonso Ruiz: Senior Software Engineer',
        'Sayid Khan: Project Manager',
    ]
