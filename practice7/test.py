import psycopg
import config

conn = psycopg.connect(
    host=config.DB_HOST,
    dbname=config.DB_NAME,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    port=config.DB_PORT
)

print("Connected successfully!")