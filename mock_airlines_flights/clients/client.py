import requests
from requests.auth import HTTPBasicAuth

API_BASE = "http://stub.2xt.com.br/air/search"
USER = "demo"
PASSWORD = "swnvlD"
API_KEY = "pzrvlDwoCwlzrWJmOzviqvOWtm4dkvuc"

class Client:
    def __init__(self, base_url=API_BASE, user=USER, password=PASSWORD, api_key=API_KEY):
        self.base_url = base_url
        self.user = user
        self.password = password
        self.api_key = api_key

    def get_flight(self, airport_from, airport_to, date) -> dict:
        """Get flight information from the API.

        Args:
            airport_from (str): The departure airport code.
            airport_to (str): The arrival airport code.
            date (str): The date of the flight in YYYY-MM-DD format.

        Returns:
            dict: The flight information.
        """
        url = f"{self.base_url}/{self.api_key}/{airport_from}/{airport_to}/{date}"
        response = requests.get(url, auth=HTTPBasicAuth(self.user, self.password), timeout=10)
        response.raise_for_status()
        return response.json()
    
client = Client()

if __name__ == "__main__":
    # Example usage
    try:
        flight_info = client.get_flight("SFO", "LAX", "2023-10-01")
        print(flight_info)
    except requests.RequestException as e:
        print(f"Error fetching flight information: {e}")