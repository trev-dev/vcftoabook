from sys import exit
from os import path
from parser import parse_vcf


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


def main(args):
    try:
        with open(path.abspath(args.input), 'r') as f:
            data = f.read().split('BEGIN:VCARD')
    except FileNotFoundError:
        exit(f'File not found: {path.abspath(args.input)}')

    parsed_data = [parse_vcf(entry) for entry in data]

    # Prune contacts with no email address entered
    contacts = list(filter(lambda x: x['email'], parsed_data))

    # Don't write anything to disk if contacts are empty
    if not contacts:
        exit('Unable to write file: Input vcf is corrupt or invalid')
    if args.output:
        with open(path.abspath(args.output), 'w+') as f:
            f.write(build_template(contacts))
    else:
        with open('./addressbook', 'w+') as f:
            f.write(build_template(contacts))
