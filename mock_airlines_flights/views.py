from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import date as dt_date
from dateutil.parser import parse

from airports_data_fetch.models import Airports
from mock_airlines_flights.serializer import (
    FlightSearchSerializer,
    FlightCombinationSerializer,
)
from mock_airlines_flights.clients.client import client
from mock_airlines_flights.services.service import service


class FlightSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        flight_serializer = FlightSearchSerializer(data=request.query_params)
        flight_serializer.is_valid(raise_exception=True)
        origin_airport, destination_airport, departure_date = (
            flight_serializer.validated_data["origin"],
            flight_serializer.validated_data["destination"],
            flight_serializer.validated_data["departure_date"],
        )
        return_date = flight_serializer.validated_data["return_date"]

        if origin_airport == destination_airport:
            return Response(
                {"error": "origin and destination cannot be the same"}, status=400
            )
        if departure_date < dt_date.today() or return_date < departure_date:
            return Response({"error": "invalid date"}, status=400)

        for airport_code in (origin_airport, destination_airport):
            if not Airports.objects.filter(iata=airport_code).exists():
                return Response(
                    {"error": f"airport {airport_code} not found."}, status=400
                )

        outbound_flights = client.get_flight(
            origin_airport, destination_airport, departure_date.strftime("%Y-%m-%d")
        )
        inbound_flights = client.get_flight(
            destination_airport, origin_airport, return_date.strftime("%Y-%m-%d")
        )

        for flight_option in outbound_flights["options"]:
            flight_option["price"] = service.calculate_price(
                flight_option["price"]["fare"]
            )
            flight_option["meta"] = service.calculate_meta(
                outbound_flights["summary"]["from"],
                outbound_flights["summary"]["to"],
                parse(flight_option["departure_time"]),
                parse(flight_option["arrival_time"]),
            )
        for flight_option in inbound_flights["options"]:
            flight_option["price"] = service.calculate_price(
                flight_option["price"]["fare"]
            )
            flight_option["meta"] = service.calculate_meta(
                inbound_flights["summary"]["from"],
                inbound_flights["summary"]["to"],
                parse(flight_option["departure_time"]),
                parse(flight_option["arrival_time"]),
            )

        flight_combinations = service.build_flights(
            outbound_flights["options"], inbound_flights["options"]
        )
        response_data = FlightCombinationSerializer(flight_combinations, many=True).data
        return Response(response_data)
