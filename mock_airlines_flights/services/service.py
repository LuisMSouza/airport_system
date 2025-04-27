from datetime import date as dt
from math import radians, sin, cos, sqrt, asin
from airports_data_fetch.models import Airport
from mock_airlines_flights.clients.client import client

class Service:
    def __init__(self, client=client):
        self.client = client

    def _harversine(self, lat1, lon1, lat2, lon2):
        """
        Calculate the great-circle distance between two points on the Earth
        specified in decimal degrees using the Haversine formula.
        """
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * asin(sqrt(a))
        r = 6371
        return c * r
    
    def _calculate_price(self, fare) -> dict:
        """
        Calculate the price of a flight based on the fare.
        """
        fee = max(fare * 0.1, 40)
        total = fare + fee
        return {
            "fare": fare,
            "fee": round(fee, 2),
            "total": round(total, 2)
        }
    
    def _calculate_meta(self, departure ,arrival, departure_time, arrival_time):
        """
        Calculate the meta information for a flight.
        """
        distance = self._harversine(departure['latitude'], departure['longitude'], 
                                    arrival['latitude'], arrival['longitude'])
        duration = (arrival_time - departure_time).total_seconds() / 3600
        approximate_speed = round(distance / duration, 2) if duration > 0 else 0
        cost_per_km = round((departure_time - arrival_time).total_seconds() and (self._calculate_price(1)["fare"] / distance), 2) if distance > 0 else 0
        return {
            "range": round(distance, 2),
            "cruise_speed_kmh": approximate_speed,
            "cost_per_km": cost_per_km, 
        }
    
    def build_flights(outbound: list, inbound: list) -> list:
        """
        Build the flight information based on the outbound and inbound flights.
        """
        flights = []
        for flight in outbound:
            for return_flight in inbound:
                total_price = flight["price"]["total"] + return_flight["price"]["total"]
                flights.append({
                    "outbound": flight,
                    "inbound": return_flight,
                    "price": {
                        "fare": round(flight["price"]["fare"] + return_flight["price"]["fare"], 2),
                        "fee": round(flight["price"]["fee"] + return_flight["price"]["fee"], 2),
                        "total": round(total_price, 2)
                    }
                })
            return sorted(flights, key=lambda x: x["price"]["total"])