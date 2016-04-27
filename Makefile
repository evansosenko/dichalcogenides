all: docs lint test

docs:
	@python setup.py build_sphinx

lint:
	@python setup.py lint

release:
	@rm -rf build dist
	@python setup.py sdist bdist_wheel
	@twine upload dist/*

test:
	@python setup.py test

.PHONY: docs test
