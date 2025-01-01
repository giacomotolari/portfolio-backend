# Dockerfile
FROM python:3.10-slim

WORKDIR /app/

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY . /app

CMD ["python", "django_project/manage.py", "runserver", "0.0.0.0:8000"]
