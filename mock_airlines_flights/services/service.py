from datetime import date as dt
from math import radians, sin, cos, sqrt, asin
from airports_data_fetch.models import Airports
from mock_airlines_flights.clients.client import client


class Service:
    def __init__(self, client=client):
        self.client = client

    def _harversine(
        self,
        departure_latitude,
        departure_longitude,
        arrival_latitude,
        arrival_longitude,
    ):
        """
        Calculate the great-circle distance between two points on the Earth
        specified in decimal degrees using the Haversine formula.
        """
        departure_latitude, departure_longitude, arrival_latitude, arrival_longitude = (
            map(
                radians,
                [
                    departure_latitude,
                    departure_longitude,
                    arrival_latitude,
                    arrival_longitude,
                ],
            )
        )

        longitude_difference = arrival_longitude - departure_longitude
        latitude_difference = arrival_latitude - departure_latitude
        a = (
            sin(latitude_difference / 2) ** 2
            + cos(departure_latitude)
            * cos(arrival_latitude)
            * sin(longitude_difference / 2) ** 2
        )
        c = 2 * asin(sqrt(a))
        earth_radius_km = 6371
        return c * earth_radius_km

    def calculate_price(self, base_fare) -> dict:
        """
        Calculate the price of a flight based on the fare.
        """
        service_fee = max(base_fare * 0.1, 40)
        total_price = base_fare + service_fee
        return {
            "fare": base_fare,
            "fee": round(service_fee, 2),
            "total": round(total_price, 2),
        }

    def calculate_meta(
        self, departure_airport, arrival_airport, departure_time, arrival_time
    ):
        """
        Calculate the meta information for a flight.
        """
        distance_km = self._harversine(
            departure_airport["latitude"],
            departure_airport["longitude"],
            arrival_airport["latitude"],
            arrival_airport["longitude"],
        )

        flight_duration_hours = (arrival_time - departure_time).total_seconds() / 3600
        approximate_speed = (
            round(distance_km / flight_duration_hours, 2)
            if flight_duration_hours > 0
            else 0
        )

        cost_per_km = (
            round(self.calculate_price(1)["fare"] / distance_km, 2)
            if distance_km > 0
            else 0
        )

        return {
            "range": round(distance_km, 2),
            "cruise_speed_kmh": approximate_speed,
            "cost_per_km": cost_per_km,
        }

    def build_flights(self, outbound_flights, inbound_flights) -> list:
        """
        Build the flight information based on the outbound and inbound flights.
        """
        combined_flights = []

        for outbound_flight in outbound_flights:
            for inbound_flight in inbound_flights:
                total_price = (
                    outbound_flight["price"]["total"] + inbound_flight["price"]["total"]
                )
                combined_flights.append(
                    {
                        "outbound": outbound_flight,
                        "inbound": inbound_flight,
                        "price": {
                            "fare": round(
                                outbound_flight["price"]["fare"]
                                + inbound_flight["price"]["fare"],
                                2,
                            ),
                            "fee": round(
                                outbound_flight["price"]["fee"]
                                + inbound_flight["price"]["fee"],
                                2,
                            ),
                            "total": round(total_price, 2),
                        },
                    }
                )

        return sorted(combined_flights, key=lambda x: x["price"]["total"])


service = Service()
