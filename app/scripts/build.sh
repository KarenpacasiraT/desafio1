#!/bin/bash

IMAGE_NAME="karenpacasira/financial-stocks:latest"

# Construir la imagen Docker
docker build -t $IMAGE_NAME .

# Iniciar sesión en Docker Hub
echo "Iniciando sesión en Docker Hub"
docker login

# Subir la imagen a Docker Hub
echo "Subiendo la imagen a Docker Hub"
docker push $IMAGE_NAME
