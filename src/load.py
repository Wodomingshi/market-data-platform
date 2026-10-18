from fred import fetch_series, clean_observations
from db import save_observations

series_id = "UNRATE"
observations = fetch_series(series_id, "2024-01-01")
rows = clean_observations(observations)
save_observations(series_id, rows)
print("Loaded", len(rows), "rows for", series_id)