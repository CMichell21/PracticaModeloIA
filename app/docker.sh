#!/bin/bash

NAME='APIPRUEBA'
#1. Construcción de la imagen docker, buscar si existe la imagen si existe se elimina y se crea otra, 
#si no existe solo se crea la nueva imagen

if docker images -q $NAME | grep -q .; then
    echo "Eliminando imagen"
    docker rmi -f $NAME
    echo "Imagen eliminada"
else
    echo "No existe imagen"
fi

echo "Creando imagen"
docker build -t $NAME .


#2. Construcción del contenedor: busca si existe el contenedor, si existe verifica si esta corriendo 
# y lo apaga luego lo elimina si no esta corriendo solo lo elimina y lo vuelve a crear, si no existe solo lo crea.

if docker ps -a --filter "name=$NAME" | grep -q .; then
    docker stop $NAME
    docker rm -f $NAME
    echo "contenedor eliminado"
else
    echo "No existe contenedor"
fi

echo "Creando contenedor"
date

docker run -d \
  -v
  --name $NAME \
  -p 8000:8000 \
  -e TZ=America/Tegucigalpa \
  $NAME

docker logs $NAME
