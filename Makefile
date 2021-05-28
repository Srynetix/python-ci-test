all: lint test

lint:
	@poetry run pre-commit run --all-files

test:
	@poetry run pytest
