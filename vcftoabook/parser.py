import re


def parse_vcf(items):
    """
    Load a given vcf, parse it and attempt to return a usable dictionary
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
