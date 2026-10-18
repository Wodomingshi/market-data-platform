import os
import requests

api_key = os.environ["FRED_API_KEY"]

url = "https://api.stlouisfed.org/fred/series/observations"
params = {
    "series_id": "UNRATE",
    "api_key": api_key,
    "file_type": "json",
    "observation_start": "2024-01-01",
}

response = requests.get(url, params=params)
print("Status:", response.status_code)

data = response.json()
print("Rows received:", len(data["observations"]))
print("First row:", data["observations"][0])
print("Last row:", data["observations"][-1])

rows = []
for obs in data["observations"]:
    if obs["value"] == ".":
        print("Skipped missing value for:", obs["date"])
        continue
    rows.append((obs["date"], float(obs["value"])))

print("Clean rows:", len(rows))
print("Last clean row:", rows[-1])
