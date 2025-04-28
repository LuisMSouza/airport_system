from math import radians, sin, cos, sqrt, asin
from mock_airlines_flights.clients.client import client
from dateutil.parser import parse


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
        self,
        departure_airport,
        arrival_airport,
        departure_time,
        arrival_time,
        fare,
    ):
        dep_lat = departure_airport["lat"]
        dep_lon = departure_airport["lon"]
        arr_lat = arrival_airport["lat"]
        arr_lon = arrival_airport["lon"]

        distance_km = self._harversine(dep_lat, dep_lon, arr_lat, arr_lon)

        flight_duration_hours = (arrival_time - departure_time).total_seconds() / 3600
        approximate_speed = (
            round(distance_km / flight_duration_hours, 2)
            if flight_duration_hours > 0
            else 0
        )

        cost_per_km = (
            round(fare / distance_km, 2) if distance_km > 0 and fare > 0 else 0
        )

        return {
            "range": round(distance_km, 2),
            "cruise_speed_kmh": approximate_speed,
            "cost_per_km": cost_per_km,
        }


    def build_flights(self, outbound_flights, inbound_flights) -> list:
        """
        Build the flight information.
        """
        combined = []
        for outbound in outbound_flights:
            for inbound in inbound_flights:
                try:
                    outbound_arrival = parse(outbound["arrival_time"])
                    inbound_departure = parse(inbound["departure_time"])

                    if inbound_departure > outbound_arrival:
                        total_fare = outbound["price"]["fare"] + inbound["price"]["fare"]
                        total_fee = outbound["price"]["fee"] + inbound["price"]["fee"]

                        combined.append(
                            {
                                "outbound": outbound,
                                "inbound": inbound,
                                "price": {
                                    "fare": round(total_fare, 2),
                                    "fee": round(total_fee, 2),
                                    "total": round(total_fare + total_fee, 2),
                                },
                            }
                        )

                except (KeyError, ValueError) as e:
                    print(f"Error processing flight combination: {str(e)}")
                    continue

        return sorted(combined, key=lambda x: x["price"]["total"])


service = Service()
