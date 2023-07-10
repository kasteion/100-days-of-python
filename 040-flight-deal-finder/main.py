# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

import os
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

SHEET_TOKEN = os.environ.get("SHEET_TOKEN")
FLIGHTS_APIKEY = os.environ.get("FLIGHTS_APIKEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
TWILIO_PHONE = os.environ.get("TWILIO_PHONE")
DEST_PHONE = os.environ.get("DEST_PHONE")

data_manager = DataManager(token=SHEET_TOKEN)
flight_search = FlightSearch(api_key=FLIGHTS_APIKEY)
notification_manager = NotificationManager(
    twilio_sid=TWILIO_SID, twilio_token=TWILIO_TOKEN, twilio_phone=TWILIO_PHONE, dest_phone=DEST_PHONE)

sheet_data = data_manager.retrieve_prices()

for price in sheet_data:
    if price["iataCode"] == "":
        iata = flight_search.retrieve_iata(price["city"])
        price["iataCode"] = iata
        print(data_manager.update_price(price))
    else:
        flights = flight_search.search_flights(price["iataCode"])
        if len(flights) > 0:
            flight = flights[0]
            if flight.price <= price["lowestPrice"]:
                notification_manager.send_price_alert(flight)