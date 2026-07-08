from app.src.services.CompararService import CompararService
from app.src.schemas.Peticion import CompararPeticion
from app.src.schemas.Respuesta import Respuesta
from fastapi import FastAPI
import logging

app=FastAPI()
service= CompararService()

#configuracion de logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.post("/peticion/entrada", response_model=Respuesta)

def CompararTexto(peticion:CompararPeticion):
    
    respuesta=service.verificarOperacion(peticion)
    print(respuesta)

    return Respuesta(codigoMensaje=respuesta["codigoMensaje"],
    descripcionMensaje=respuesta["mensaje"],
    iguales=respuesta["resultado"]["iguales"],
    similitud=respuesta["resultado"]["similitud"])



