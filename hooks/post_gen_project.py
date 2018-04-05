#!/usr/bin/env python

import os

try:
    import requests
except ModuleNotFoundError:
    make_request = False
else:
    make_request = True

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def _make_request(url):
    r = requests.get(url)

    if r.ok:
        return r.text
    else:
        print('Unable to update __main__.py because of a {} response from {}: {}'.format(r.status_code, url, r.text))
        return None


def update_file(url, file):
    """Update the given file with the content from a given url."""
    content = _make_request(url)

    if content is not None:
        with open(os.path.join(PROJECT_DIRECTORY, '{{ cookiecutter.project_slug }}/{}'.format(file)), 'w') as f:
            f.write(content)


if __name__ == '__main__':
    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if make_request:
        update_file('https://raw.githubusercontent.com/ThreatConnect-Inc/tcex/master/tcex/__main__.py', '__main__.py')
        update_file('https://raw.githubusercontent.com/ThreatConnect-Inc/tcex/master/tcex/tcex_json_schema.json', 'tcex_json_schema.json')
