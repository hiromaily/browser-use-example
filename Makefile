#------------------------------------------------------------------------------
# Only Initial install
#------------------------------------------------------------------------------
.PHONY: install-python
install-python:
	asdf plugin add python
	asdf install python 3.12.8
	asdf local python 3.12.8
	python -V

# https://python-poetry.org/docs/#installing-with-the-official-installer
.PHONY: install-poetry
install-poetry:
	curl -sSL https://install.python-poetry.org | python3 -
	poetry --version

.PHONY: create-project
create-project:
	poetry new browser-use-example
	#poetry init

.PHONY: install-dependencies
install-dependencies:
	poetry add browser-use playwright
	poetry add python-dotenv argparse
	poetry add -D flake8 black isort mypy pytest
	poetry add --group dev Flake8-pyproject

.PHONY: install-playwright
install-playwright:
	poetry run playwright install

#------------------------------------------------------------------------------
# Install after clone project
#------------------------------------------------------------------------------
.PHONY: set-env
set-env:
	poetry env use 3.12.8
	poetry install

#------------------------------------------------------------------------------
# dev
#------------------------------------------------------------------------------
.PHONY: lint
lint:
	@# format import
	poetry run isort src
	@# format by PEP8
	poetry run black src
	@# lint
	poetry run flake8 src

# run price_monitoring task
.PHONY: run
run:
	poetry run python src/main.py

# .PHONY: run
# run:
# 	poetry run python src/main.py --task foobar
