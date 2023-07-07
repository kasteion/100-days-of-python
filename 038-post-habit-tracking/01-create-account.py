import requests
import os

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_USER = os.environ.get("PIXELA_USER")


data = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post("https://pixe.la/v1/users", json=data)
response.raise_for_status()
print(response.text)
