from app.models.log_proceso import LogProceso
from app.models.log_peticion_respuesta import LogPeticionRespuesta
from app.service.validar_service import ValidarServicio
from app.repository.log_proceso_repository import LogProcesoRepository
from app.repository.log_peticion_repository import LogPeRepository
#from app.service.texto_comparar_service import TextoCompararService
from app.core.logger import getLogger
from app.service.validar_entrada import ValidarEntrada
from datetime import datetime, timezone
from app.core.except_personalizada import ServicioNoDisponible, ErrorDatosDeEntrada, ErrorConexionBD
import json
import uuid

class CompararService:
     
    def __init__(self):
            self.logger=getLogger()
            self.validar_servicio= ValidarServicio()
            #self.comparar=TextoCompararService()
            self.log_repository=LogProcesoRepository()
            self.logpe_repository=LogPeRepository()
            self.validar_entrada=ValidarEntrada()
    


    async def ejecutar_proceso(self, datos_entrada):
        id_log=str(uuid.uuid4())
        respuesta=None
        try:
            self.logger.info(datos_entrada)

            fecha_peticion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            json_peticion = json.dumps(datos_entrada, ensure_ascii=False)

            self.logpe_repository.insertar(
                LogPeticionRespuesta(
                    id_log,
                    json_peticion,
                    "",
                    fecha_peticion,
                    fecha_peticion,
                )
            )
            self.logger.info("ANTES DE LOG PETICION")
            self.log_repository.insertar(
                LogProceso(
                    id_log,
                    "INFO",
                    "**** INICIO DEL PROCESO ****",
                    "",
                    "ejecutar_proceso",
                    self.__class__.__name__,
                    "OK"
                )
            )

            
            peticion= self.validar_entrada.validar(datos_entrada,id_log)
            
        
            servicio=self.validar_servicio.validar(peticion.servicio,peticion.usuario,id_log)
            
           
            if servicio == "comparar_texto":
                self.logger.info("servicio encontrado exitosamente")

            respuesta_api={
                "mensaje": "procesamiento exitoso"
            }
            respuesta=json.dumps(respuesta_api)
            return respuesta_api
        
        except ErrorConexionBD as error:

            raise
        
        except ErrorDatosDeEntrada as error:
            respuesta= f"{error.codigo}:{error.mensaje}"
            self.log_repository.insertar(
                LogProceso(
                    id_log,
                    "WARNING",
                    f"{error.codigo}:{error.mensaje}",
                    "transformapi",
                    error.metodo,
                    error.clase,
                    "ALERTA"
                ))
            raise 

        except ServicioNoDisponible as error:
            respuesta=f"{error.codigo}:{error.mensaje}"
            self.log_repository.insertar(
                LogProceso(
                    id_log,
                    "WARNING",
                    f"{error.codigo}:{error.mensaje}",
                    error.usuario,
                    error.metodo,
                    error.clase,
                    "ALERTA"
                ))
            
            raise

        except Exception as error: 
            respuesta= str(error)
            self.log_repository.insertar(
                LogProceso(
                    id_log,
                    "ERROR",
                    str(error),
                    "transformapi",
                    "ejecutar_proceso",
                    self.__class__.__name__,
                    "ERROR"

                )
            )
            raise

        finally:
            try:
                self.log_repository.insertar(
                    LogProceso(
                        id_log,
                        "INFO",
                        "**** FIN DEL PROCESO ****",
                        "",
                        "ejecutar_proceso",
                        self.__class__.__name__,
                        "OK"
                    )
                )

                fecha_respuesta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.logpe_repository.actualizar(
                    LogPeticionRespuesta(
                        id_log,
                        "",
                        respuesta,
                        fecha_respuesta,
                        fecha_respuesta
                    ))
            except Exception as error:

                self.logger.error(f"no se pudo conectar a la base de datos{error}")
            

        



        

