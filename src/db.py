import os
import psycopg


def save_observations(series_id, rows):
    """Insert (date, value) rows for one series. Safe to run repeatedly."""
    sql = """
        INSERT INTO macro_observations (series_id, obs_date, value)
        VALUES (%s, %s, %s)
        ON CONFLICT (series_id, obs_date) DO NOTHING
    """
    params = [(series_id, obs_date, value) for obs_date, value in rows]
    with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
        with conn.cursor() as cur:
            cur.executemany(sql, params)