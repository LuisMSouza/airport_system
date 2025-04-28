.PHONY: build up down logs shell migrate makemigrations superuser collectstatic test requirements help

# Project variables
PROJECT_NAME = airport_sistem

help:
    @echo "Available commands:"
    @echo "  make build            - Build Docker containers"
    @echo "  make up               - Start Docker containers"
    @echo "  make down             - Stop Docker containers"
    @echo "  make logs             - View Docker container logs"
    @echo "  make shell            - Open a shell in the web container"
    @echo "  make migrate          - Run Django migrations"
    @echo "  make makemigrations   - Create new Django migrations"
    @echo "  make superuser        - Create a Django superuser"
    @echo "  make collectstatic    - Collect static files"
    @echo "  make test             - Run tests"
    @echo "  make requirements     - Update requirements.txt"

# Docker commands
build:
    docker-compose build

up:
    docker-compose up -d

down:
    docker-compose down

logs:
    docker-compose logs -f

shell:
    docker-compose exec web python manage.py shell

# Django commands
migrate:
    docker-compose exec web python manage.py migrate

makemigrations:
    docker-compose exec web python manage.py makemigrations

superuser:
    docker-compose exec web python manage.py createsuperuser

collectstatic:
    docker-compose exec web python manage.py collectstatic --noinput

test:
    docker-compose exec web python manage.py test

# Update requirements
requirements:
    docker-compose exec web pip freeze > requirements.txt
