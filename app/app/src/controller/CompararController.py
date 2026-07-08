#from app.src.services.CompararService import CompararService
from app.src.schemas.Peticion import CompararPeticion
from app.src.schemas.Respuesta import CompararRespuesta
from fastapi import FastAPI

app=FastAPI()
#service= CompararService()

@app.post("/peticion/entrada", response_model=Respuesta)
def CompararTexto(peticion:CompararPeticion):
    #service(peticion)
    return Respuesta(codigoMensaje="000",
    descripcionMensaje="ghghj",
    iguales="si",
    similitud=100)



