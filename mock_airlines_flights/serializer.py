from rest_framework import serializers


class FlightSearchSerializer(serializers.Serializer):
    origin = serializers.CharField(max_length=3)
    destination = serializers.CharField(max_length=3)
    departure_date = serializers.DateField()
    return_date = serializers.DateField()


class FlightOptionSerializer(serializers.Serializer):
    departure_time = serializers.DateTimeField()
    arrival_time = serializers.DateTimeField()
    price = serializers.DictField()
    meta = serializers.DictField()


class FlightCombinationSerializer(serializers.Serializer):
    outbound = FlightOptionSerializer()
    inbound = FlightOptionSerializer()
    price = serializers.DictField()
