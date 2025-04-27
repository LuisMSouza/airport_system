from rest_framework import serializers
from airports_data_fetch.models import Airports

class AirportSerializer(serializers.ModelSerializer):
    """
    Serializer for the Airport model.
    """
    class Meta:
        model = Airports
        fields = '__all__'