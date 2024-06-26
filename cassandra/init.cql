-- Création du keyspace
CREATE KEYSPACE IF NOT EXISTS weather_data
WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

-- Création de la table
CREATE TABLE IF NOT EXISTS weather_data.weather (
    city TEXT,
    timestamp TIMESTAMP,
    temperature FLOAT,
    humidity FLOAT,
    PRIMARY KEY (city, timestamp)
);

