from django.db import transaction
from models import Airports

class AirportRepository:
    """
    Repository class for managing airport data.
    """
    def __init__(self, model=Airports):
        self.model = model

    def upsert_airports(self, airports_data):
        """
        Upserts a list of airports into the database.
        """
        with transaction.atomic():
            for airport in airports_data:
                self.model.objects.update_or_create(
                    iata=airport['iata'],
                    defaults={
                        'city': airport['city'],
                        'latitude': airport['latitude'],
                        'longitude': airport['longitude'],
                        'state': airport['state']
                    }
                )

airport_repository = AirportRepository()
