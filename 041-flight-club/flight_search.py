import requests
import datetime as dt
from flight_data import FlightData
import pprint as pp


class FlightSearch:
    def __init__(self, api_key: str):
        self.key = api_key
        self.url = "https://api.tequila.kiwi.com"
        self.locations_endpoint = "/locations/query"
        self.search_endpoint = "/v2/search"

    def retrieve_iata(self, city: str) -> str:
        headers = {
            "apiKey": self.key
        }
        parameters = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(f"{self.url}{self.locations_endpoint}", headers=headers, params=parameters)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def search_flights(self, dest: str):
        date_from = dt.datetime.today() + dt.timedelta(days=1)
        date_to = dt.date.today() + dt.timedelta(days=6*30)
        headers = {
            "apiKey": self.key
        }
        parameters = {
            "fly_from": "LON",
            "fly_to": dest,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "max_stopovers": 0,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP",
        }
        response = requests.get(f"{self.url}{self.search_endpoint}", headers=headers, params=parameters)
        response.raise_for_status()
        data = response.json()["data"]
        flights = [
            FlightData(
                price=d["price"],
                departure_airport=d["flyFrom"],
                departure_city=d["cityFrom"],
                dest_airport=d["flyTo"],
                dest_city=d["cityTo"],
                date_from=d["route"][0]["utc_departure"].split("T")[0],
                date_to=d["route"][1]["utc_departure"].split("T")[0]
            ) for d in data
        ]
        if len(flights) == 0:
            parameters["max_stopovers"] = 2
            response = requests.get(f"{self.url}{self.search_endpoint}", headers=headers, params=parameters)
            response.raise_for_status()
            data = response.json()["data"]
            flights = [
                FlightData(
                    price=d["price"],
                    departure_airport=d["flyFrom"],
                    departure_city=d["cityFrom"],
                    dest_airport=d["flyTo"],
                    dest_city=d["cityTo"],
                    date_from=d["route"][0]["utc_departure"].split("T")[0],
                    date_to=d["route"][-1]["utc_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=d["route"][0]["cityTo"]
                ) for d in data
            ]

        return flights
