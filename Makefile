SHELL := /bin/bash

dev: requirements.txt
		@( \
				test -d ./venv || virtualenv --python=python2.7 ./venv; \
				. ./venv/bin/activate; \
				pip install -r requirements.txt; \
		)
		@echo
		@echo '**Now you should `source ./venv/bin/activate` to activate your virtualenv**'
		@echo

.PHONY: dev
