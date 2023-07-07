import requests
import datetime as dt
import os

PIXELA_USER = os.environ.get("PIXELA_USER")
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH = "graph1"

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

data = {
    "quantity": "30"
}

date = dt.datetime.now().strftime("%Y%m%d")
response = requests.put(f"https://pixe.la/v1/users/{PIXELA_USER}/graphs/{GRAPH}/{date}", headers=headers, json=data)
response.raise_for_status()
print(response.text)
