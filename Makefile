help:
	@echo make env
	@echo make run

env:
	@pipenv shell

install:
	pipenv install --pre prefect

run:
	python main.py
