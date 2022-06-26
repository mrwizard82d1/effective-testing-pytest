#!/usr/bin/env python

"""Formats data for display."""


def format_data_for_display(people):
    return [f'{person["given_name"]} {person["family_name"]}: {person["title"]}'
            for person in people]


def format_data_for_excel(people):
    return [f'{person["given_name"]},{person["family_name"]},"{person["title"]}"'
            for person in people]
