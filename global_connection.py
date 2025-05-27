import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

# Create and export global connection
try:
    connection = mysql.connector.connect(**DB_CONFIG)
    if connection.is_connected():
        print("MySQL connection established.")
    else:
        print("Failed to connect.")
except mysql.connector.Error as e:
    print("Connection Error:", e)
    connection = None
