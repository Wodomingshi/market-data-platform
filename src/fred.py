import os
import requests

URL = "https://api.stlouisfed.org/fred/series/observations"


def fetch_series(series_id, start_date):
    """Fetch raw observations for one FRED series."""
    params = {
        "series_id": series_id,
        "api_key": os.environ["FRED_API_KEY"],
        "file_type": "json",
        "observation_start": start_date,
    }
    response = requests.get(URL, params=params)
    if response.status_code != 200:
        raise RuntimeError(f"FRED request failed, status {response.status_code}")
    return response.json()["observations"]


def clean_observations(observations):
    """Convert text values to numbers, skip and report missing ones."""
    rows = []
    for obs in observations:
        if obs["value"] == ".":
            print("Skipped missing value for:", obs["date"])
            continue
        rows.append((obs["date"], float(obs["value"])))
    return rows


observations = fetch_series("UNRATE", "2024-01-01")
rows = clean_observations(observations)
print("Clean rows:", len(rows))
print("Last clean row:", rows[-1])



