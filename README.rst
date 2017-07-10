*****************
TCEX App Template
*****************

.. image:: https://api.codacy.com/project/badge/Grade/5e95a4486c7048f6bd74132e167becaf
   :alt: Codacy Badge
   :target: https://www.codacy.com/app/fhightower/tcex-app-template

A template for quickly building `TCEX Apps <https://github.com/ThreatConnect-Inc/tcex>`_  using `cookiecutter <https://github.com/audreyr/cookiecutter>`_ .

Usage
=====

This package is designed to be used with `cookiecutter <https://github.com/audreyr/cookiecutter>`_ . Installing cookiecutter can be as easy as:

``pip install cookiecutter``

but there are other options as well (see the `cookiecutter documentation <https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter>`_ ).

Once cookiecutter is installed, simply run the following command which will prompt you for some values (which it will use to fill out the template) and create a new, ready-to-go directory for your TCEX App in the current working directory.

.. code-block:: shell

    # This will ask you to give some input values and will then create a basic
    # package for you based on those values in the current directory.
    $ cookiecutter https://github.com/fhightower/tcex-app-template.git

Once the template is cloned and you've started writing code, you can update the app's version using `bumpversion <https://pypi.python.org/pypi/bumpversion>`_ (available via: ``pip install bumpversion``). Running ``bumpversion patch`` will automatically increment the patch version number in ``{{ cookiecutter.project_slug }}/__init__.py`` and ``{{ cookiecutter.project_slug }}/install.json``. ``bumpversion minor`` will increment the minor version number in the same places and ``bumpversion major`` will do the same with the major version number.
