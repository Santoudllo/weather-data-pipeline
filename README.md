# weather-data-pipeline

Ce projet démontre un pipeline de données qui récupère les données météorologiques d'une API, les traite et les stocke dans une base de données Cassandra. L'ensemble est conteneurisé avec Docker et orchestré avec Kubernetes.

## Structure du Projet

- **app.py** : Script Python pour récupérer les données météorologiques de l'API OpenWeatherMap et les stocker dans Cassandra.
- **requirements.txt** : Dépendances Python du projet.
- **Dockerfile** : Dockerfile pour conteneuriser l'application Python.
- **kubernetes/** : Fichiers de déploiement et de service Kubernetes pour Cassandra et l'application Python.
  - **cassandra-deployment.yaml** : Configuration de déploiement pour Cassandra.
  - **cassandra-service.yaml** : Configuration de service pour Cassandra.
  - **api-deployment.yaml** : Configuration de déploiement pour l'application Python.
  - **api-service.yaml** : Configuration de service pour l'application Python.
  - **cronjob.yaml** : Configuration de CronJob pour exécuter le script Python à intervalles réguliers.

## Prise en Main

### Prérequis

- Docker
- Cluster Kubernetes (par exemple, Minikube)
- `kubectl` configuré pour accéder à votre cluster Kubernetes

### Configuration

1. **Construire et pousser l'image Docker** :
   ```sh
   docker build -t your_dockerhub_username/weather-api .
   docker push your_dockerhub_username/weather-api
