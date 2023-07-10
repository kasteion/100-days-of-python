import requests


class DataManager:
    def __init__(self, token: str):
        self.token = token
        self.url = "https://api.sheety.co/a3a7667cd4673d4ec7c8f671312c9eba"
        self.prices_endpoint = "/flightDeals/prices"
        self.users_endpoint = "/flightDeals/users"

    def retrieve_prices(self):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(f"{self.url}{self.prices_endpoint}", headers=headers)
        response.raise_for_status()
        return response.json()["prices"]

    def update_price(self, price):
        object_id = price["id"]
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        body = {
            "price": price
        }
        response = requests.put(f"{self.url}{self.prices_endpoint}/{object_id}", headers=headers, json=body)
        response.raise_for_status()
        return response.text
