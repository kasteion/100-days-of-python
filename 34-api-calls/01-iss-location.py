import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
# Status Codes
# 1XX: Hold on
# 2XX: Here you go
# 3XX: Go Away - Redirect
# 4XX: You screwed up
# 5XX: I screwed up
response.raise_for_status()
data = response.json()
position = (data["iss_position"]["longitude"], data["iss_position"]["latitude"])
print(position)
