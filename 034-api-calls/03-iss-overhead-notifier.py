import time
import requests
import datetime as dt
import smtplib
import os

MY_LAT = 14.641980
MY_LNG = -90.513237

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")


def iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])

    if not ((MY_LAT - 5 < iss_lat < MY_LAT + 5) and (MY_LAT - 5 < iss_lng < MY_LNG + 5)):
        return False

    return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    now = dt.datetime.now().hour - 6

    if not sunset < now < sunrise:
        return False

    return True


look_up = False

while not look_up:
    if is_night() and iss_overhead():
        look_up = True

        with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
            conn.starttls()
            conn.login(user=EMAIL, password=PASSWORD)
            conn.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg="Subject:Look up!\nThe ISS is above you in the sky!")
    else:
        print("Don't look up")
    time.sleep(60)
