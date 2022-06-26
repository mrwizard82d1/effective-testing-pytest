#!/usr/bin/env python

"""Formats data for display."""


def format_data_for_display(people):
    return [f'{person["given_name"]} {person["family_name"]}: {person["title"]}'
            for person in people]


def format_data_for_excel(people):
    header = ','.join([key.replace('_name', '') for key in people[0].keys()])
    data = [f'{person["given_name"]},{person["family_name"]},"{person["title"]}"'
            for person in people]
    raw_result = [header]
    raw_result.extend(data)
    result = '\n'.join(raw_result)
    return result
