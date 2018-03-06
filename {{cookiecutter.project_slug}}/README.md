# {{ cookiecutter.project_name.title() }}

{% if cookiecutter.runtime_level == 'Playbook' %}## Summary

{{ cookiecutter.project_description }}

## Dependencies

- tcex

## Input Definitions

Todo: add input definitions

## Output Definitions

Todo: add output definitions

## Use Cases

Todo: add use cases{% else %}## Usage

Todo: add instructions here{% endif %}

## Installing in ThreatConnect

To install this app in ThreatConnect, run:

```shell
make lib
make pack
```

This will create a `.tcx` file in the top app directory which will work in ThreatConnect assuming the instance of ThreatConnect is running the same version of python used during the `make lib` command.

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and [Floyd Hightower's TCEX App Template](https://github.com/fhightower-templates/tcex-app-template).
