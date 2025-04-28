web: gunicorn airport_system.wsgi:application --bind 0.0.0.0:$PORT
celery: celery -A airport_system worker --loglevel=info