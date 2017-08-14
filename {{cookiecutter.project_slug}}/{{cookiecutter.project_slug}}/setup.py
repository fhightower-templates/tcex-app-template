import json
from setuptools import setup, find_packages

with open('install.json', 'r') as fh:
    version = json.load(fh)['programVersion']

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    author='{{ cookiecutter.author_name }}',
    description='{{ cookiecutter.project_description }}',
    install_requires=[
        # TODO: Add required packages here...
        'tcex'
    ],
    license='{{ cookiecutter.open_source_license }}',
    name='{{ cookiecutter.project_slug }}',
    packages=find_packages(),
    version=version
)
