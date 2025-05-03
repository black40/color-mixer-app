# Makefile для проекта на Python с Poetry и Kivy/KivyMD

# Запуск приложения
run:
	poetry run python app/main.py

# Форматирование и линтинг кода с помощью Ruff
lint:
	poetry run ruff check .

# Автоисправление проблем с Ruff (если возможно)
fix:
	poetry run ruff check . --fix

# Установка зависимостей (включая dev-группу)
install_dev:
	poetry install --with dev

# Обновление зависимостей
update:
	poetry update

# Удаление виртуального окружения (если надо перезапустить всё с нуля)
reset:
	poetry env remove python

# Установка pre-commit хуков
hooks:
	poetry run pre-commit install

# Запуск pre-commit хуков на всех файлах
precommit:
	poetry run pre-commit run --all-files
