web: gunicorn --bind 0.0.0.0:$PORT airport_sistem.wsgi:application
celery: celery -A airport_sistem worker --loglevel=info