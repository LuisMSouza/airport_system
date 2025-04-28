from rest_framework import viewsets
from .serializer import AirportSerializer
from airports_data_fetch.models import Airports

class AirportViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Airports.
    """
    queryset = Airports.objects.all()
    serializer_class = AirportSerializer