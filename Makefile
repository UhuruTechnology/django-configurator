# Shortcuts for project testing and development using make
#
UV = uv
PIP = pip3
TOX = tox


#: help - Display callable targets.
.PHONY: help
help:
	@echo "django-configurator make shortcuts"
	@echo "Here are available targets:"
	@egrep -o "^#: (.+)" [Mm]akefile  | sed 's/#: /* /'


#: develop - Install all development utilities for Python3.
.PHONY: develop
develop:
	$(UV) sync --all-extras --dev --group test
	$(UV) tool install pre-commit --with pre-commit-uv --force-reinstall
	pre-commit install


#: clean - Basic cleanup, mostly temporary files.
.PHONY: clean
clean:
	find . -name "*.pyc" -delete
	find . -name '*.pyo' -delete
	find . -name "__pycache__" -delete


#: distclean - Remove local builds, such as *.egg-info.
.PHONY: distclean
distclean: clean
	rm -rf *.egg
	rm -rf *.egg-info
	rm -rf demo/*.egg-info
	rm -rf configurator/attachments/
	# remove the django-created database
	find . -name \*.sqlite3 -delete


#: maintainer-clean - Remove almost everything that can be re-generated.
.PHONY: maintainer-clean
maintainer-clean: distclean
	rm -rf build/
	rm -rf dist/
	rm -rf .tox/


#: test - Run test suites.
.PHONY: test
test:
	$(UV) run $(TOX) r


#: format - Run the PEP8 formatter.
.PHONY: format
format:
	uv tool run ruff check --fix # Fix linting errors
	uv tool run ruff format # fix formatting errors


#: checkformat - checks formatting against configured format specifications for the project.
.PHONY: checkformat
checkformat:
	uv tool run ruff check # linting check
	uv tool run ruff format --check # format check


#: documentation - Build documentation (Sphinx, README, ...).
.PHONY: documentation
documentation: sphinx readme


#: sphinx - Build Sphinx documentation (docs).
.PHONY: sphinx
sphinx:
	$(TOX) -e sphinx


#: readme - Build standalone documentation files (README, CONTRIBUTING...).
.PHONY: readme
readme:
	$(TOX) -e readme


#: release - Tag and push to PyPI.
.PHONY: release
release:
	$(TOX) -e release

