all: help

.PHONY: help clean install-dev uninstall-dev test build upload

PYPI_REPO ?= testpypi

help:   
	@echo "help          - show this help"
	@echo "clean         - remove Python artifacts"
	@echo "install-dev   - install for development"
	@echo "uninstall-dev - uninstall package"
	@echo "reinstall-dev - reinstall (clean install)"
	@echo "test          - run tests"
	@echo "build         - build package"
	@echo "upload        - upload to PYPI_REPO (default: testpypi)"

clean:  
	@find . -name '*.py[cod]' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -rf {} +
	@find . -name '*$py.class' -exec rm -rf {} +
	@rm -rf build/ dist/ *.egg-info .pytest_cache/ .coverage htmlcov/
	@rm -rf src/*.egg-info/

install-dev:
	pip install -e ".[dev]"

uninstall-dev:
	pip uninstall -y {{ cookiecutter.package_name }}

reinstall-dev: uninstall-dev install-dev

test:
	pytest tests/ -xvs

build:
	python -m build

upload: build
	twine check dist/* && twine upload --repository $(PYPI_REPO) dist/*
