from app.core.logger import getLogger
from fastapi import HTTPException
from app.models.log_proceso import LogProceso
from app.repository.log_proceso_repository import LogProcesoRepository
from app.core.except_personalizada import ServicioNoDisponible


class ValidarServicio:
    logger= getLogger()
    log_repository=LogProcesoRepository()


    def __init__(self):
        self.servicios= {
            1: "comparar_texto"
        }

    def validar(self, servicio, usuario, uuid):
            
        servicio_validado= self.servicios.get(servicio)
        
        if servicio_validado is None:
            raise ServicioNoDisponible (400,"servicio no habilitado", usuario,"validar",self.__class__.__name__)
        

        self.log_repository.insertar(
                LogProceso(
                    uuid,
                    "INFO",
                    "servicio habilitado",
                    usuario,
                    "validar",
                    self.__class__.__name__,
                    "OK"
                ))
        
        return servicio_validado