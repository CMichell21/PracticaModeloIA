from fastapi import APIRouter, Depends, status, Request
router = APIRouter(prefix="/transformapi", tags=["Comparar"])

import json

from app.service.comparar_orquestador import CompararService

orquestador = CompararService()


@router.post("/comparar")
def comparar (request: Request):

    peticion= await request.json

    resultado= await orquestador.control_flujo(peticion)   
    
    return 


from app.schemas.peticion import Peticion
from app.models.log_proceso import LogProceso
from app.service.validar_service import ValidarServicio
from app.repository.log_proceso_repository import LogProcesoRepository
from app.repository.log_peticion_repository import LogPeticonResRepository
from app.models.log_peticion_respuesta import LogPeticionRespuesta
#from app.service.texto_comparar_service import TextoCompararService
from app.core.logger import getLogger
from app.service.validar_entrada import ValidarEntrada

class CompararService:

    def __init__(self):
            self.logger=getLogger()
            self.validar_servicio= ValidarServicio()
            #self.comparar=TextoCompararService()
            self.log_repository=LogProcesoRepository()
            self.log_pere_repository=LogPeticonResRepository()
            self.validar_entrada=ValidarEntrada()
    


    async def control_flujo(self, datos_entrada):
        try:
            self.log_pere_repository.insertar(
                LogProceso(
                    uuid,
                    "INFO",
                    "INICIO DEL PROCESO",
                    datos_entrada.usurio,
                    "ejecutar",
                    self.__class__.__name__,
                    "OK"
                )
            )

            peticio= self.validar_entrada.validar(datos_entrada)

            #servicio=self.validar_servicio.validar(peticion.servicio)

        except:   
        
        finally:
            self.logs.insertar(
                LogProceso(
                    uuid,
                    "INFO",
                    "FIN DEL PROCESO",
                    usuario,
                    "ejecutar",
                    self.__class__.__name__,
                    "OK"
                )
            ) from app.schemas.peticion import Peticion
from pydantic import ValidationError
from app.repository.log_proceso_repository import LogProcesoRepository
from app.log_proceso import LogProceso
from app.log_peticion_respuesta import LogPeticionRespuesta
from app.log_peticion_repository import LogPeticonResRepository
from datetime import datetime, timezone

class ValidarEntrada:

    Log_repository = LogProcesoRepository()
    Log_petres_repository= LogPeticonResRepository()


    def validar(self, datos_entrada):
        try:
            fecha_peticion= datetime.now(timezone.utc)

            self.Log_petres_repository.insertar(
                LogPeticonResRepository(
                    uuid,
                    datos_entrada,
                    ""
                    fecha_peticion,
                    fecha_peticion,
                )
            )

            peticion= Peticion(**datos_entrada)

            return peticion.CuerpoPeticion

        
        except ValidationError as error:
            self.log_repository.insertar(
                LogProceso(
                    uuid,
                    "ERROR",
                    f"Dato no coincide con los esperadors{}"
                    peticion.peticion.usuario,
                    "ejecutar",
                    self.__class__.__name__,
                    "ERROR"

                )
            )
            
            fecha_respuesta= datetime.now(timezone.utc)
            self.Log_petres_repository.actualizar(
                LogPeticonResRepository(
                    error,
                    fecha_respuesta,
                )
            )
            raise Exception(f"datos no validos: {error}")



