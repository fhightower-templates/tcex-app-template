*****************
TCEX App Template
*****************

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

Installing in ThreatConnect
===========================

To install an app created with this template in ThreatConnect, run:

.. code-block:: shell

    make lib
    make pack

This will create a ``.tcx`` file in the top app directory which will work in ThreatConnect assuming that your instance of ThreatConnect has the same version of python that was used during the ``make lib`` command.
