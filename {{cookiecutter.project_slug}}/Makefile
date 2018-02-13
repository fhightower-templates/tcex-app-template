.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-tcx clean-build clean-pyc clean-test ## remove all tcex, build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

clean-tcx: ## remove tcx artifacts
	rm -fr ./{{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}-package.log
	rm -fr ./{{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}-libs.log

lint: ## check style with flake8
	flake8 {{ cookiecutter.project_slug }} tests

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: clean ## package and upload a release
	python setup.py sdist upload
	python setup.py bdist_wheel upload

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l DIST

install: clean ## install the package to the active Python's site-packages
	cd ./{{ cookiecutter.project_slug }} && python setup.py install

lib: clean ## download required packages into a lib directory
	cd ./{{ cookiecutter.project_slug }} && tclib

pack: clean ## package the app for deployment to TC
	cd ./{{ cookiecutter.project_slug }} && tcpackage --outdir ../

collection: clean ## package the app for deployment to TC as part of a collection of apps
	cd ./{{ cookiecutter.project_slug }} && python app.py --package --collection --zip_out ..

validate: clean ## validate the app's install.json
	python ./{{ cookiecutter.project_slug }}/app.py --validate --install_json ./{{ cookiecutter.project_slug }}/install.json

run: clean ## run the app locally
	cd ./{{ cookiecutter.project_slug }} && tcrun

test: clean ## run tests on the app
	pytest
