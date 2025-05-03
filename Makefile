run:
	poetry run python app/main.py

install:
	poetry install

format:
	poetry run black .

lint:
	poetry run flake8 .

format_ruff:
	ruff check --fix
	ruff format
