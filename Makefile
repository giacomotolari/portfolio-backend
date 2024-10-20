start-docker:
	  @echo "Starting Docker Compose..."
	  docker-compose up 

stop-docker:
	  @echo "Stopping Docker Compose..."
	  docker-compose -f docker-compose.yml down

make-migrations:
	  @echo "Creating Django migrations..."
	  poetry run python manage.py makemigrations

migrate:
	  @echo "Running Django migrations..."
	  poetry run python manage.py migrate

start-django:
	  @echo "Starting Django server..."
	  poetry run python manage.py runserver

redis-cli:
	  @echo "Connecting to Redis CLI..."
	  docker exec -it giaco-dev-backend-redis-1 redis-cli
