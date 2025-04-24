from celery import shared_task
from clients.domestic_airports import domestic_airports_client
from repository.airport_repository import airport_repository

ENDPOINT_URL = 'https://stub.amopromo.com/air/airports/pzrvlDwoCwlzrWJmOzviqvOWtm4dkvuc'  # URL da API de aeroportos

@shared_task
def fetch_airports_data():
    """
    Celery task to fetch airports data from an Domestic Airports API and update the database.
    """
    airports = domestic_airports_client.fetch_airports_data()
    airport_repository.upsert_airports(airports)
    return f"Fetched and updated {len(airports)} airports data."
