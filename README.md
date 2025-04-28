# Airport System API

## 📋 Requisitos
- Docker
- Python 3.9+

## 🚀 Instalação Local
```bash
docker-compose up --build
```

## 🔐 Autenticação


Inclua o token no header das requisições:

```http
Authorization: Token 0f13051c97472f76dfe17696bab8d385c735b2a0
```

## 🌐 Endpoints

### Buscar Voos (Mock Airlines)
GET /api/mock-airlines/search/

Parâmetros:
- `origin`: Código IATA (ex: GRU)
- `destination`: Código IATA (ex: GIG)
- `departure_date`: Data de ida (YYYY-MM-DD)
- `return_date`: Data de volta (YYYY-MM-DD)

Exemplo:

```bash
curl -H "Authorization: Token 0f13051c97472f76dfe17696bab8d385c735b2a0" "http://localhost:8000/api/mock-airlines/search/?origin=GRU&destination=GIG&departure_date=2024-05-20&return_date=2024-05-25"
```

### Atualizar Aeroportos
Executa automaticamente às 00:00 via Celery.

## ☁️ Hospedagem
URL da API:
https://nome-do-seu-app.herokuapp.com

## 🛠️ Tecnologias Utilizadas
- Django
- Django REST Framework
- Celery
- Redis
- Docker
- PostgreSQL