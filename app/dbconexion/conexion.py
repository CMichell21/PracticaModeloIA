from app.core.except_personalizada import ErrorConexionBD
from app.core.config import config 
import jaydebeapi
from app.core.logger import getLogger 

class Conexion:

    def __init__(self):
        self.logger=getLogger(__name__)

    def Conectar(self):

        try:
            conn= jaydebeapi.connect(
                config.DB_DRIVER,
                f"jdbc:{config.URL}",
                [config.DB_USER, config.DB_PASSWORD],
                config.DB_JAR
                )

            self.logger.info("conexion exitosa")

            return conn

        except Exception as error :
                                  
            raise ErrorConexionBD(f"no se pudo obtener la conexion: {error}")
            

            
            
    

    


            
            
    

    
