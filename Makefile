help:
	@echo "update 		Update files from the tcex repo (https://github.com/ThreatConnect-Inc/tcex)"

update:  # update the file from the main tcex repo
	# clone the tcex repo
	git clone https://github.com/ThreatConnect-Inc/tcex;
	# copy app.py
	cp ./tcex/tcex/app.py ./\{\{cookiecutter.project_slug\}\}/\{\{cookiecutter.project_slug\}\}/
	# copy __main__.py
	cp ./tcex/tcex/__main__.py ./\{\{cookiecutter.project_slug\}\}/\{\{cookiecutter.project_slug\}\}/
	# copy tcex_json_schema.json
	cp ./tcex/tcex/tcex_json_schema.json ./\{\{cookiecutter.project_slug\}\}/\{\{cookiecutter.project_slug\}\}/
	# remove the tcex repo
	rm -rf ./tcex/
