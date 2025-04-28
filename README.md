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
Authorization: Token 3b77a634ada844c07f20eb9f80d4610145d7d806
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
curl --location 'https://airportsistem-eaa1fefe93b7.herokuapp.com/api/mock-airlines/search/?origin=GRU&destination=GIG&departure_date=2026-05-20&return_date=2026-05-25' --header 'Authorization: Token 3b77a634ada844c07f20eb9f80d4610145d7d806'
```

### Atualizar Aeroportos
Executa automaticamente às 00:00 via Celery.

## ☁️ Hospedagem
URL da API:
https://airportsistem-eaa1fefe93b7.herokuapp.com

## 🛠️ Tecnologias Utilizadas
- Django
- Django REST Framework
- Celery
- Redis
- Docker
- PostgreSQL