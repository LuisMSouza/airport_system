web: gunicorn airport_sistem.wsgi:application --bind 0.0.0.0:$PORT
celery: celery -A airport_sistem worker --loglevel=info