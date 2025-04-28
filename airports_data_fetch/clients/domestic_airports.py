import requests

class DomesticAirportsClient:
    """
    Client to fetch domestic airports data from an API.
    """
    ENDPOINT_URL = 'https://stub.amopromo.com/air/airports/pzrvlDwoCwlzrWJmOzviqvOWtm4dkvuc'

    def __init__(self):
        self.headers = {
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Basic ZGVtbzpzd252bEQ=',  # User and password encoded in Base64
            'priority': 'u=0, i',
            'referer': 'https://gist.github.com/',
            'sec-ch-ua': 'Google',
            'sec-ch-ua-arch': 'x86',
            'sec-ch-ua-bitness': '64',
            'sec-ch-ua-full-version-list': 'Google',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '',
            'sec-ch-ua-platform': 'Windows',
            'sec-ch-ua-platform-version': '19.0.0',
            'sec-ch-ua-wow64': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
        }

    def fetch_airports_data(self):
        """
        Fetches airports data from the API and returns it as a list of dictionaries.
        """
        try:
            response = requests.get(self.ENDPOINT_URL, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error while fetching data: {e}")
            return []
        
domestic_airports_client = DomesticAirportsClient()