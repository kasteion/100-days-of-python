import requests
import datetime as dt
import os

PIXELA_USER = os.environ.get("PIXELA_USER")
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH = "graph1"

headers = {
    "X-USER-TOKEN": PIXELA_USER
}

date = dt.date.today().strftime("%Y%m%d")

response = requests.delete(f"https://pixe.la/v1/users/{PIXELA_USER}/graphs/{GRAPH}/{date}", headers=headers)
response.raise_for_status()
print(response.text)
