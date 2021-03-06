PACKAGE_NAME=femethods

.PHONY: install docs lint-html tests
.PHONY: build

docs:
	cd docs && make html

install:
	python setup.py install

lint:
	black $(PACKAGE_NAME) --line-length=79
	isort -rc $(PACKAGE_NAME)
	pylint $(PACKAGE_NAME)

lint-tests:
	black tests --line-length=79
	isort -rc tests
	pylint tests

tests:
	pytest --cov-report html --cov=$(PACKAGE_NAME) tests/$(PACKAGE_NAME)

tests-ci:
	pytest --cov-report html --cov=$(PACKAGE_NAME) tests/$(PACKAGE_NAME) -v

build:
	python setup.py sdist
	python setup.py bdist_wheel

upload:
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
