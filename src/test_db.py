import os
import psycopg

conn = psycopg.connect(os.environ["DATABASE_URL"])

with conn.cursor() as cur:
    cur.execute("SELECT version()")
    print(cur.fetchone())

conn.close()