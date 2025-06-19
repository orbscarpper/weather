import requests
import csv
from datetime import datetime
import os

API_KEY = os.getenv("API_KEY")
CITY = "New York"
FILENAME = "weather_data.csv"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
if response.status_code != 200:
    raise Exception(f"API error: {response.status_code}")

data = response.json()

entry = {
    "timestamp": datetime.utcnow().isoformat(),
    "city": CITY,
    "temperature": data["main"]["temp"],
    "humidity": data["main"]["humidity"],
    "weather": data["weather"][0]["description"]
}

file_exists = os.path.isfile(FILENAME)

with open(FILENAME, mode="a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=entry.keys())
    if not file_exists:
        writer.writeheader()
    writer.writerow(entry)
