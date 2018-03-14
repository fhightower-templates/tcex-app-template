# -*- coding: utf-8 -*-
"""{{ cookiecutter.project_description }}"""

import traceback

from tcex import TcEx


def parse_arguments():
    """Parse arguments coming into the app."""
    tcex.parser.add_argument('--string', help='Input string', required=True)
    return tcex.args


def main():
    """."""
    args = parse_arguments()
    {% if cookiecutter.runtime_level == 'Playbook' %}
    # read the string from the playbook to get the actual value of the argument
    string = tcex.playbook.read(args.string)

    tcex.log.info('String value: {}'.format(string))

    # output the reversed string to downstream playbook apps
    tcex.playbook.create_output('{{cookiecutter.project_slug}}.reversed_string', string[::-1])
    {% elif cookiecutter.runtime_level == 'Organization' %}
    tcex.log.info('String value: {}'.format(args.string))
    tcex.message_tc('Reversed string: {}'.format(args.string[::-1]))
    {% endif %}
    tcex.exit(0)


if __name__ == "__main__":
    tcex = TcEx()
    try:
        # start the app
        main()
    except SystemExit:
        pass
    except Exception as e:  # if there are any strange errors, log it to the logging in the UI
        err = 'Generic Error.  See logs for more details ({}).'.format(e)
        tcex.log.error(traceback.format_exc())
        tcex.message_tc(err)
        tcex.playbook.exit(1)
