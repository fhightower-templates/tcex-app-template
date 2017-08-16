# -*- coding: utf-8 -*-
"""{{ cookiecutter.project_description }}."""

import traceback

from tcex import TcEx


def parse_arguments():
    """Parse arguments coming into the app."""
    # retrieve a string as an argument
    tcex.parser.add_argument('--string', help='Input string', required=True)
    args = tcex.args

    return args


def main():
    """."""
    # handle the incoming arguments
    args = parse_arguments()

    # TODO: Add your code here!

    # exit
    tcex.exit()


if __name__ == "__main__":
    # initialize a TcEx instance
    tcex = TcEx()
    try:
        # start the app
        main()
    except SystemExit:
        pass
    except:  # if there are any strange errors, log it to the logging in the UI
        err = 'Generic Error. See logs for more details.'
        tcex.log.error(traceback.format_exc())
        tcex.message_tc(err)
        tcex.playbook.exit(1)
