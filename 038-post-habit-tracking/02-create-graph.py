import requests
import os

PIXELA_USER = os.environ.get("PIXELA_USER")
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

data = {
    "id": "graph1",
    "name": "meditation graph",
    "unit": "Minutes",
    "type": "int",
    "color": "ajisai"
}

response = requests.post(f"https://pixe.la/v1/users/{PIXELA_USER}/graphs", headers=headers, json=data)
response.raise_for_status()
print(response.text)
