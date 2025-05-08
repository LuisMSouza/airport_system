FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8000 \
    DJANGO_SETTINGS_MODULE=airport_system.settings.production \
    DATABASE_URL=sqlite:///db.sqlite3

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput && \
    python manage.py makemigrations && \
    python manage.py migrate

CMD gunicorn \
    --bind 0.0.0.0:$PORT \
    --workers 3 \
    --timeout 120 \
    airport_system.wsgi:application