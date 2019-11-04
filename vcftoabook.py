#!/usr/bin/env python

import re
import argparse


def parse_data(items):
    """
    Parse strings from vcf data and attempt to return the type and data
    """
    items = list(filter(lambda x: x != '', items.split('\n')))

    entry = {
        'name': '',
        'email': set(),
        'notes': ''
    }

    for item in items:
        if 'FN:' in item:
            entry['name'] = item.split(':')[1]
        elif 'EMAIL;' in item:
            entry['email'].add(item.split(':')[1])
        elif 'NOTE:' in item:
            entry['notes'] = re.search(r'NOTE:(.+)', item).group(1)

    return entry


def build_template(data):
    """
    Build and return an addressbook file template
    """
    template = (
        '# abook addressbook file\n\n'
        '[format]\n'
        'program=abook\n'
        'version=0.6.1\n\n'
    )

    for index, entry in enumerate(data):
        template += (
            f'\n[{index}]\n'
            f'name={entry["name"]}\n'
            f'email={",".join(entry["email"])}\n'
        )
        if entry["notes"]:
            template += f'notes={entry["notes"]}\n'
    template += '\n'
    return template


"""
with open('./contacts.vcf', 'r') as f:
    data = f.read().split('BEGIN:VCARD')

parsed_data = [parse_data(entry) for entry in data]

# Prune contacts with no email address entered
contacts = list(filter(lambda x: x['email'], parsed_data))

# Save re-formatted contacts to disk
with open('./addressbook', 'w+') as f:
    f.write(build_template(contacts))
"""

parser = argparse.ArgumentParser(
    prog="vcftoabook",
    description="Convert .vcf files into addressbook files to be used in "
                "abook/Mutt"
)

parser.add_argument(
    '-i', '--input',
    metavar='input',
    type=str,
    help="the input path of a .vcf file"
)

parser.add_argument(
    '-o', '--output',
    metavar="output",
    type=str,
    default='addressbook',
    help="the output path/filename (default: ./addressbook)"
)

args = parser.parse_args()

if args.input:
    print(f'Convert {args.input}')
