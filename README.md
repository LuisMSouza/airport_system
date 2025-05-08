# Airport System API

## 📋 Requirements
- Docker
- Python 3.9+
- Docker Compose (for local environment)

## ☁️ Hosting
**API URL:**  
https://airportsistem-eaa1fefe93b7.herokuapp.com

## 🔐 Authentication

Include the token in request headers:

```http
Authorization: Token 3b77a634ada844c07f20eb9f80d4610145d7d806
```

## 🌐 Endpoints

### 🔍 Search Flights (Mock Airlines)
GET /api/mock-airlines/search/

Parameters:
- `origin`: IATA Code (ex: GRU)
- `destination`: IATA Code (ex: GIG)
- `departure_date`: Departure date (YYYY-MM-DD)
- `return_date`: Return date (YYYY-MM-DD)

Example:

```bash
curl --location 'https://airportsystem-82ef0b028080.herokuapp.com/api/mock-airlines/search/?origin=GRU&destination=GIG&departure_date=2026-05-20&return_date=2026-05-25' \
--header 'Authorization: Token 3b77a634ada844c07f20eb9f80d4610145d7d806'
```

### 🛫 Update Airports Database
- **Automatic**: Runs daily at 00:00 via Celery
- **Manual**: Execute via CLI:

```bash
docker-compose exec web python manage.py fetch_airports
```

## 🛠️ Technologies Used
| Technology | Function |
|------------|----------|
| Django | Main framework |
| Django REST | REST API |
| Celery + Redis | Asynchronous tasks and queues |
| PostgreSQL | Main database |
| Docker | Containerization and isolated environment |

## 🚀 Development Setup

### ⚙️ Makefile Commands
```bash
# Project initialization
make build       # Build containers
make up          # Start services
make down        # Stop services

# Dependency management
make requirements  # Update requirements.txt

# Database
make migrate       # Apply migrations
make makemigrations  # Create new migrations

# Utilities
make superuser    # Create admin user
make test         # Run unit tests
make shell        # Open Django shell
```

### 🔄 Basic Workflow
1. Configure the environment:
```bash
make build && make up
```

2. Apply migrations:
```bash
make migrate
```

3. Create a superuser:
```bash
make superuser
```

4. Run tests:
```bash
make test
```
