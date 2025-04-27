.PHONY: build up down logs shell migrate makemigrations superuser collectstatic test heroku-login heroku-create heroku-push heroku-release heroku-deploy heroku-logs requirements help

# Project variables
PROJECT_NAME = airport_sistem
HEROKU_APP_NAME = $(PROJECT_NAME)

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
    @echo "  make heroku-login     - Login to Heroku CLI"
    @echo "  make heroku-create    - Create Heroku app"
    @echo "  make heroku-push      - Push Docker image to Heroku"
    @echo "  make heroku-release   - Release the application on Heroku"
    @echo "  make heroku-deploy    - Full Heroku deployment (push + release)"
    @echo "  make heroku-logs      - View Heroku logs"

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

# Heroku commands
heroku-login:
    heroku login

heroku-create:
    heroku create $(HEROKU_APP_NAME) || true
    heroku addons:create heroku-redis:hobby-dev -a $(HEROKU_APP_NAME)

heroku-push:
    heroku container:login
    heroku container:push web -a $(HEROKU_APP_NAME)

heroku-release:
    heroku container:release web -a $(HEROKU_APP_NAME)
    heroku run python manage.py migrate -a $(HEROKU_APP_NAME)
    heroku run python manage.py collectstatic --noinput -a $(HEROKU_APP_NAME)

heroku-deploy: heroku-push heroku-release

heroku-logs:
    heroku logs --tail -a $(HEROKU_APP_NAME)