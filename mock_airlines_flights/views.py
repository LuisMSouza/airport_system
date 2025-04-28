from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import date as dt_date
from dateutil.parser import parse
from .serializer import FlightSearchSerializer, FlightCombinationSerializer
from .clients.client import client
from .services.service import service
from airports_data_fetch.models import Airports


class FlightSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        flight_serializer = FlightSearchSerializer(data=request.query_params)
        flight_serializer.is_valid(raise_exception=True)
        validated_data = flight_serializer.validated_data

        origin = validated_data["origin"]
        destination = validated_data["destination"]
        departure_date = validated_data["departure_date"]
        return_date = validated_data["return_date"]

        today = dt_date.today()
        if departure_date < today or return_date < departure_date:
            return Response({"error": "Invalid date range"}, status=400)

        try:
            origin_airport = Airports.objects.get(iata=origin)
            destination_airport = Airports.objects.get(iata=destination)
        except Airports.DoesNotExist:
            return Response({"error": "Airport not found"}, status=404)

        try:
            outbound_response = client.get_flight(
                origin, destination, departure_date.strftime("%Y-%m-%d")
            )
            inbound_response = client.get_flight(
                destination, origin, return_date.strftime("%Y-%m-%d")
            )
        except Exception as e:
            return Response({"error": f"Flight API error: {str(e)}"}, status=503)

        def process_flights(response):
            processed = []
            for flight in response.get("options", []):
                try:
                    departure = parse(flight["departure_time"].replace(" ", "T"))
                    arrival = parse(flight["arrival_time"].replace(" ", "T"))

                    fare = flight["price"]["fare"]
                    meta = service.calculate_meta(
                        response["summary"]["from"],
                        response["summary"]["to"],
                        departure,
                        arrival,
                        fare,
                    )

                    processed.append(
                        {
                            "departure_time": departure.isoformat(),
                            "arrival_time": arrival.isoformat(),
                            "price": service.calculate_price(fare),
                            "meta": meta,
                        }
                    )
                except Exception as e:
                    print(f"Skipping invalid flight: {str(e)}")
            return processed

        processed_outbound = process_flights(outbound_response)
        processed_inbound = process_flights(inbound_response)

        flight_combinations = service.build_flights(processed_outbound, processed_inbound)

        if not flight_combinations:
            return Response({"warning": "No valid flight combinations found"}, status=404)

        serializer = FlightCombinationSerializer(flight_combinations, many=True)
        return Response(serializer.data)
