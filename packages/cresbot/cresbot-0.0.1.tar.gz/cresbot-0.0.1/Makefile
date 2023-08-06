# ------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------


PYTHON = python3
BLACK  = black
TWINE  = twine

FILES  = cresbot tests setup.py

all: help
.PHONY: all


help:
.PHONY: help


register:
	$(PYTHON) setup.py register
.PHONY: register

venv:
	$(PYTHON) -m venv $@
	source $@/bin/activate
	pip install pip --upgrade
	pip install setuptools --upgrade
	pip install setuptools_scm --upgrade
	pip install wheel --upgrade


build:
	$(PYTHON) setup.py sdist bdist_wheel
.PHONY: build


upload:
	$(TWINE) upload --config $(PWD)/.pypirc dist/*
.PHONY: upload


format:
	$(BLACK) --line-length 100 $(FILES)
.PHONY: format


clean:
	rm -rf \
		build dist *.egg-info \
		$$(find . -type d -name __pycache__) \
		.tox
.PHONY: clean
