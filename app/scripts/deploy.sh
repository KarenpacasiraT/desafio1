#!/bin/bash

IMAGE_NAME="karenpacasira/financial-stocks:latest"

# Descargar la imagen desde Docker Hub
docker pull $IMAGE_NAME

# Ejecutar el contenedor
docker run -d -p 5000:5000 $IMAGE_NAME

# Mostrar la URL para acceder a la aplicación
echo "La aplicación está disponible en http://localhost:5000"
