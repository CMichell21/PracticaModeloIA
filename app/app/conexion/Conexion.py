import jaydebeapi
from app.core.Logger import getLogger
import os
import time
from dotenv import load_dotenv

load_dotenv()

class Conexion:
    def __init__(self, registrar_log=True):

        self.registrar_log = registrar_log
        self.logger = getLogger(__name__)

    def obtenerConexion(self):
        inicio= time.perf_counter()
        try:
            conn= jaydebeapi.connect(os.getenv('DRIVER_NAME'),
                             f"jdbc:{os.getenv('URL')}",
                             [os.getenv('DBUSER'),os.getenv('DBPASSWORD')],
                             os.getenv("DIR_DRIVER")
                             )
            
            fin= time.perf_counter()
            
            tiempo=fin-inicio

            if tiempo >= float(os.getenv('TIEMPO_CONEXION')):
                if self.registrar_log:
                    self.logger.warning(
                        "Conexion exitosa pero tardo más de lo esperado",
                    extra={
                        "usuario":"Prueba",
                        "clase":self.__class__.__name__,
                        "metodo":"obtenerConexion",
                        "detalle": f"tiempo:{tiempo} segundos"
                    }
                )
                return conn
            
            if self.registrar_log:
                self.logger.info(
                    "Conexion exitosa",
                    extra={
                        "usuario":"Prueba",
                        "clase":self.__class__.__name__,
                        "metodo":"obtenerConexion",
                        "detalle":"Ninguno"
                    }
                )

            return conn
        
        except Exception as e :
            if self.registrar_log:
                self.logger.error(
                    f"No se pudo obtener la conexion{e}",
                    extra={
                        "usuario":"Prueba",
                        "clase":self.__class__.__name__,
                        "metodo":"obtenerConexion",
                        "detalle": str(e)
                    }
                )
            
            raise Exception("Conexion fallida") from e

    
