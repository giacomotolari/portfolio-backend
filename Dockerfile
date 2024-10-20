# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
