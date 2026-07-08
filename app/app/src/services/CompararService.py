from app.src.models.PeticionModel import Peticion
from app.modeloIA1.modeloIA import modeloIA
from fastapi import HTTPException
from dotenv import load_dotenv
import os

class CompararService:
    def __init__(self):
        self.modelo = modeloIA()

    def CompararTexto(self,peticion:Peticion):

        umbral= float(os.getenv("UMBRAL"))
        resultado=self.modelo.procesar_similitud_del_coseno(peticion.textoA,peticion.textoB,umbral)
        
        return resultado

   