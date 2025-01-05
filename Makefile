# Docker commands (production)

docker-prod-start:
	@echo "Starting Docker Compose..."
	@docker-compose up 

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

docker-dev-delete:
	@echo "Deleting Docker Compose in development mode..."
	@docker-compose -f docker-compose.dev.yml down -v

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

django-migrate-app-to-migration:
	@echo "Migrating Django app to specific migration..."
	@poetry run python3 django_project/manage.py migrate $(app_name) $(migration_name)

django-run:
	@echo "Starting Django server..."
	@poetry run python3 django_project/manage.py runserver

django-create-superuser:
	@echo "Creating Django superuser..."
	@poetry run python3 django_project/manage.py createsuperuser

django-create-app:
	@echo "Creating Django app..."
	@poetry run python3 django_project/manage.py startapp $(app_name)

redis-cli:
	@echo "Connecting to Redis CLI..."
	@docker exec -it giaco-dev-backend-redis-1 redis-cli

# Postgres commands

tables = auth_group auth_group_permissions auth_permission auth_user auth_user_groups \
         auth_user_user_permissions companies_customercompany companies_employercompany \
         django_admin_log django_content_type django_migrations django_session \
         projects_asemployeeproject projects_asemployeeproject_customer_companies \
         projects_personalproject projects_teamopensourceproject projects_teamprivateproject 


pg-backup-table:
	@echo "Backing up Postgres table..."
	@docker exec -it giaco-dev-backend-db-1 pg_dump -U giaco-dev-user-dev -d giaco-dev-db-dev -t $(table_name) > db/$(table_name).sql

pg-restore-table:
	@echo "Restoring Postgres table..."
	@docker exec -i giaco-dev-backend-db-1 psql -U giaco-dev-user-dev -d giaco-dev-db-dev < db/$(table_name).sql

pg-restore-all:
	@echo "Restoring Postgres database..."
	@docker exec -i giaco-dev-backend-db-1 psql -U giaco-dev-user-dev -d giaco-dev-db-dev < db/all_tables.sql

pg-restore-each-table:
	@echo "Restoring each Postgres table..."
	@for table in $(tables); do \
		echo "Restoring Postgres table $$table..."; \
		docker exec -i giaco-dev-backend-db-1 psql -U giaco-dev-user-dev -d giaco-dev-db-dev < db/$$table.sql; \
	done

pg-backup-each-table:
	@echo "Backing up each Postgres table..."
	@for table in $(tables); do \
		echo "Backing up Postgres table $$table..."; \
		docker exec -it giaco-dev-backend-db-1 pg_dump -U giaco-dev-user-dev -d giaco-dev-db-dev -t $$table > db/$$table.sql; \
	done

pg-backup-all:
	@echo "Backing up Postgres database..."
	@docker exec -it giaco-dev-backend-db-1 pg_dump -U giaco-dev-user-dev -d giaco-dev-db-dev > db/all_tables.sql


# General commands

format:
	@echo "Formatting code..."
	@black .
