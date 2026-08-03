from app.schemas.peticion import Peticion
from pydantic import ValidationError
from app.repository.log_proceso_repository import LogProcesoRepository
from app.models.log_proceso import LogProceso
from app.core.except_personalizada import ErrorDatosDeEntrada


class ValidarEntrada:
    log_repository=LogProcesoRepository()

    def validar(self, datos_entrada,uuid):
        try:
            
            peticion= Peticion(**datos_entrada)

            if peticion != None:
                self.log_repository.insertar(
                LogProceso(
                    uuid,
                    "INFO",
                    "validacion de datos de entrada exitosa",
                    peticion.peticion.usuario,
                    "ejecutar_proceso",
                    self.__class__.__name__,
                    "OK"
                )
            )

            return peticion.peticion

        
        except ValidationError as error:
            
            raise ErrorDatosDeEntrada(400,f"El parametro ingresado no coincide: {error.errors()}","validar", self.__class__.__name__)


