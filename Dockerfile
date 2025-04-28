FROM python:3.12-slim

ENV PORT=8000

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "gunicorn airport_system.wsgi:application --bind 0.0.0.0:$PORT"]