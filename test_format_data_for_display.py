#!/usr/bin/env python

"""Tests formatting data for display."""



from format_data import (
    format_data_for_display,
    format_data_for_excel,
)



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




def test_format_for_excel():
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

    expect = '\n'.join(['given,family,title',
                        'Alfonso,Ruiz,"Senior Software Engineer"',
                        'Sayid,Khan,"Project Manager"'])
    assert format_data_for_excel(people) == expect
