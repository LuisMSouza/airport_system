from django.core.management.base import BaseCommand
from airports_data_fetch.clients.domestic_airports import domestic_airports_client
from airports_data_fetch.repository.airport_repository import airport_repository

class Command(BaseCommand):
    help = 'Fetch airports data from the Domestic Airports API and update the database.'

    def handle(self, *args, **kwargs):
        """
        Handle the command to fetch airports data.
        """
        self.stdout.write("Fetching airports data...")
        airports = domestic_airports_client.fetch_airports_data()
        airport_repository.upsert_airports(airports)
        self.stdout.write(f"Fetched and updated {len(airports)} airports data.")