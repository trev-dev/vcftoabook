import re


def parse_vcf(items):
    """
    Parse data from a vcf and attempt to return a usable dictionary
    """
    items = list(filter(lambda x: x != '', items.split('\n')))

    entry = {
        'name': '',
        'email': set(),
        'notes': '',
        'custom1': ''
    }

    for item in items:
        if 'FN:' in item:
            entry['name'] = item.split(':')[1]
        elif 'EMAIL;' in item:
            entry['email'].add(item.split(':')[1])
        elif 'NOTE:' in item:
            entry['notes'] = re.search(r'NOTE:(.+)', item).group(1)
        elif 'UID:' in item:
            entry['custom1'] = item.split(':')[1]

    return entry


def parse_abook(contacts):
    """
    Parse data from an abook file and return a usable dictionary
    """
    pass
