import requests
from cassandra.cluster import Cluster
from datetime import datetime

# Configuration de l'API et Cassandra
API_KEY = '****'
CITY = 'Paris'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

# Connexion à Cassandra
cluster = Cluster(['cassandra'])
session = cluster.connect()

# Création du keyspace et de la table si ce n'est pas déjà fait
session.execute("""
CREATE KEYSPACE IF NOT EXISTS weather_data
WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
""")
session.execute("""
CREATE TABLE IF NOT EXISTS weather_data.weather (
    city TEXT,
    timestamp TIMESTAMP,
    temperature FLOAT,
    humidity FLOAT,
    PRIMARY KEY (city, timestamp)
)
""")

# Récupération des données
response = requests.get(URL)
data = response.json()

# Extraction des données nécessaires
city = data['name']
temperature = data['main']['temp']
humidity = data['main']['humidity']
timestamp = datetime.now()

# Insertion dans Cassandra
query = "INSERT INTO weather_data.weather (city, timestamp, temperature, humidity) VALUES (%s, %s, %s, %s)"
session.execute(query, (city, timestamp, temperature, humidity))

print(f"Data inserted for {city} at {timestamp}")
