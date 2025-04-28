# Airport System API

## 📋 Requirements
- Docker
- Python 3.9+

## 🚀 Local Installation
```bash
docker-compose up --build
```

## 🔐 Authentication

Include the token in request headers:

```http
Authorization: Token 3b77a634ada844c07f20eb9f80d4610145d7d806
```

## 🌐 Endpoints

### Search Flights (Mock Airlines)
GET /api/mock-airlines/search/

Parameters:
- `origin`: IATA Code (ex: GRU)
- `destination`: IATA Code (ex: GIG)
- `departure_date`: Departure date (YYYY-MM-DD)
- `return_date`: Return date (YYYY-MM-DD)

Example:

```bash
curl --location 'https://airportsystem-82ef0b028080.herokuapp.com/api/mock-airlines/search/?origin=GRU&destination=GIG&departure_date=2026-05-20&return_date=2026-05-25' --header 'Authorization: Token 3b77a634ada844c07f20eb9f80d4610145d7d806'
```

### Update Airports
Runs automatically at 00:00 via Celery.

## ☁️ Hosting
API URL:
https://airportsistem-eaa1fefe93b7.herokuapp.com

## 🛠️ Technologies Used
- Django
- Django REST Framework
- Celery
- Redis
- Docker
- PostgreSQL