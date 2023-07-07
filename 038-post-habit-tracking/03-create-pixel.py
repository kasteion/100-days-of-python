import requests
import time
import os

PIXELA_USER = os.environ.get("PIXELA_USER")
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH = "graph1"

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

data = {
    "date": time.strftime("%Y%m%d", time.localtime()),
    "quantity": "15"
}

response = requests.post(f"https://pixe.la/v1/users/{PIXELA_USER}/graphs/{GRAPH}", headers=headers, json=data)
response.raise_for_status()
print(response.text)
