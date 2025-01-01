# Docker commands (production)

docker-prod-start:
	@echo "Starting Docker Compose..."
	@docker-compose up 

docker-prod-stop:
	@docker-compose -f docker-compose.dev.yml down

docker-prod-stop:
	@echo "Stopping Docker Compose..."
	@docker-compose -f docker-compose.yml down


# Docker commands (development)

docker-dev-start:
	@echo "Starting Docker Compose in development mode..."
	@docker-compose -f docker-compose.dev.yml up

# Use when updating the Dockerfile
docker-dev-start-build:
	@echo "Starting Docker Compose in development mode with build..."
	@docker-compose -f docker-compose.dev.yml up --build

docker-dev-stop:
	@echo "Stopping Docker Compose in development mode..."
	@docker-compose -f docker-compose.dev.yml down

docker-dev-exec-db:
	@echo "Connecting to Postgres CLI..."
	@docker exec -it giaco-dev-backend-db-1 psql -U giaco-dev-user-dev -d giaco-dev-db-dev

# Django commands

django-make-migrations:
	@echo "Creating Django migrations..."
	@poetry run python3 django_project/manage.py makemigrations

django-migrate:
	@echo "Running Django migrations..."
	@poetry run python3 django_project/manage.py migrate

django-run:
	@echo "Starting Django server..."
	@poetry run python3 django_project/manage.py runserver

django-create-superuser:
	@echo "Creating Django superuser..."
	@poetry run python3 django_project/manage.py createsuperuser

redis-cli:
	@echo "Connecting to Redis CLI..."
	@docker exec -it giaco-dev-backend-redis-1 redis-cli
