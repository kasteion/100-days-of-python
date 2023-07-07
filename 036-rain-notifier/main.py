import requests
import os
from twilio.rest import Client

OW_APPID = os.environ.get("OW_APPID")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
TWILIO_PHONE = os.environ.get("TWILIO_PHONE")
PHONE = os.environ.get("PHONE")

parameters = {
    "lat": 14.64198,
    "lon": -90.513237,
    "cnt": 8,
    "appid": OW_APPID
}

res = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
res.raise_for_status()

bring_umbrella = False

for weather_data in res.json()["list"]:
    weather = weather_data["weather"]
    for w in weather:
        if w["id"] < 700:
            bring_umbrella = True
    if bring_umbrella:
        break

if bring_umbrella:
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    message = client.messages.create(
        body="Bring an umbrella",
        from_=TWILIO_PHONE,
        to=PHONE,
    )
    print(message.status)
