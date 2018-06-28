*****************
TCEX App Template
*****************

PROJECT MOVED TO GITLAB: https://gitlab.com/fhightower-templates. 

-----

.. image:: https://api.codacy.com/project/badge/Grade/c6de421bb24442b6b3955defc0170c3d
    :alt: Codacy Badge
    :target: https://www.codacy.com/app/fhightower/tcex-app-template

A template for quickly building quality `TCEX Apps <https://github.com/ThreatConnect-Inc/tcex>`_ using `cookiecutter <https://github.com/audreyr/cookiecutter>`_.

Prerequisites
=============

1. **cookiecutter (required)**

You will need to install `cookiecutter <https://github.com/audreyr/cookiecutter>`_ . This can be as easy as:

``pip install cookiecutter``

but there are other options available in the `cookiecutter documentation <https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter>`_ .

2. **bumpversion (optional)**

`Bumpversion <https://pypi.python.org/pypi/bumpversion>`_ is really handy for incrementing version numbers. This app template is designed to work with bumpversion so that typing ``bumpversion patch``, ``bumpversion minor``, or ``bumpversion major`` will automatically increment the patch version number in ``{{ cookiecutter.project_slug }}/__init__.py`` and ``{{ cookiecutter.project_slug }}/install.json``. You can read more about bumpversion `here <https://github.com/peritus/bumpversion#bumpversion>`_.

Usage
=====

To quickly create a TCEX app (which will be created in a directory in the current working directory), run:

.. code-block:: shell

    cookiecutter https://github.com/fhightower-templates/tcex-app-template.git

Running this command will ask you a few questions about the app (like the author's name, project name, and initial vesion number). Once, you're done, it will have created a directory in the current working directory with the contents of the app.

The directory structure of the new app will look something like:

- <APP-SLUG>
    - **.bumpversion.cfg** - Manage `bumpversion <https://pypi.python.org/pypi/bumpversion>`_
    - **.editorconfig** - See `http://editorconfig.org/ <http://editorconfig.org/>`_
    - **.gitignore**
    - **Makefile** - `Makefile <https://en.wikipedia.org/wiki/Makefile>`_ with commands for packing, preparing, and testing the app
    - **README.md**
    - <APP-SLUG> - Directory containing the contents of the app
        - **__init__.py** - Basic details about the app
        - **__main__.py** - Default file from `https://github.com/ThreatConnect-Inc/tcex/blob/master/tcex/__main__.py <https://github.com/ThreatConnect-Inc/tcex/blob/master/tcex/__main__.py>`_
        - **<APP-SLUG>.py** - This app contains the actual content of the app
        - **install.json** - Provides details about how the app will be configured (see `https://docs.threatconnect.com/en/latest/deployment_config.html <https://docs.threatconnect.com/en/latest/deployment_config.html>`_)
        - **requirements.txt** - List out the packages required to run package
        - **setup.cfg** - This file is a work-around for a `known bug <https://stackoverflow.com/questions/24257803/distutilsoptionerror-must-supply-either-home-or-prefix-exec-prefix-not-both>`_ in python installed using homebrew
        - **setup.py** - Standard `setup.py <https://github.com/kennethreitz/setup.py>`_
        - **tcex.json** - Provide details for testing the app locally (see `https://docs.threatconnect.com/en/latest/tcex/building_apps.html#profile-format <https://docs.threatconnect.com/en/latest/tcex/building_apps.html#profile-format>`_)
        - **tcex_json_schema.json** - File from `https://github.com/ThreatConnect-Inc/tcex/blob/master/tcex/tcex_json_schema.json <https://github.com/ThreatConnect-Inc/tcex/blob/master/tcex/tcex_json_schema.json>`_ to validate the format of the install.json
    - **tests/** - Directory for holding tests for the app

The key is that the app's contents are placed in ``<APP-SLUG>/<APP-SLUG>/<APP-SLUG>.py``. The configuration of the app is managed in ``<APP-SLUG>/<APP-SLUG>/install.json``. And the parameters used for local testing are provided in ``<APP-SLUG>/<APP-SLUG>/tcex.json``.

Now, move into the app's directory.

.. code-block:: shell

    ls
    cd /<APP-SLUG>

To view the commands provided by the make file, run: ``make``. To setup an environment for testing run: ``make profile``. Then, to `build local modules <https://docs.threatconnect.com/en/latest/tcex/building_apps.html#build-local-modules>`_ for testing the app, run: ``make lib``. Now you are ready to run the app locally. To do this, run: ``make run``. This will create a directory in ``<APP-SLUG>/<APP-SLUG>/log/`` with any `logs <https://docs.threatconnect.com/en/latest/tcex/logging.html>`_ and `messages <https://docs.threatconnect.com/en/latest/tcex/message_tc.html>`_.

There are a few make commands that are particularly useful:

- ``make clean``: remove all tcex, build, test, coverage and Python artifacts
- ``make lib``: download required packages into a lib directory
- ``make pack``: package the app for deployment to TC
- ``make run``: run the app locally
- ``make profile``: create a tcex.json profile for the app
- ``make test``: run tests on the app

Installing in ThreatConnect
===========================

To install an app created with this template in ThreatConnect, run:

.. code-block:: shell

    make lib
    make pack

This will create a ``.tcx`` file in the top app directory which will work in ThreatConnect assuming that your instance of ThreatConnect has the same version of python that was used during the ``make lib`` command.
