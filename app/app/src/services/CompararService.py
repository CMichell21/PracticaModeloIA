from app.src.models.Peticion import Peticion
from app.modeloIA1.ModeloIaComparar import  ModeloIaComparar
from fastapi import HTTPException
from dotenv import load_dotenv
from app.src.schemas.TextoComparar import TextoComparar
import os
import logging


class CompararService:

    
    modelo = ModeloIaComparar()
    log= logging.getLogger(__name__)

    def __init__(self):
        self.operaciones = {
            1: self.CompararTexto,
        }

    def verificarOperacion(self, peticion):
        try:
            operacion = self.operaciones.get(peticion.peticion.servicio)
            self.log.info("operacion{operacion}")

            if operacion is None:
                return {
                    "codigoMensaje": "01",
                    "mensaje": "Operacion no existente",
                    "resultado": None
                }

            resultado=operacion(peticion)

            return {
                "codigoMensaje": "00",
                "mensaje": "Proceso exitoso",
                "resultado": resultado
            }


        except ValueError as e:
           return e 
        


    def CompararTexto(self, peticion):
        try:
            umbral = float(os.getenv("UMB_COMP", 0.8))

            textos = TextoComparar(
                textoA=peticion.peticion.textoA,
                textoB=peticion.peticion.textoB
            )

            resultado = self.modelo.procesar_similitud_del_coseno(textos, umbral)

            return resultado
        except Exception as e:
            raise e 
        
