from app.core.cargar_propiedades import CargarPropiedades
import jaydebeapi
from app.core.logger import getLogger 

class Conexion:

    def __init__(self):
        self.propiedades= CargarPropiedades()
        self.logger=getLogger(__name__)


    def Conectar(self):

        try:
            driver= self.propiedades.obtener_propiedades('NAME_CLASS')
            url= self.propiedades.obtener_propiedades('URL')
            user= self.propiedades.obtener_propiedades('DB_USER')
            password= self.propiedades.obtener_propiedades('DB_PASSWORD')
            addres_driver= self.propiedades.obtener_propiedades('ADDRES_DRIVER')

            conn= jaydebeapi.connect(
                driver,
                f"jdbc:{url}",
                [user, password],
                addres_driver
                )

            self.logger.info("conexion exitosa")

            return conn

        except Exception as e :
                                  
            self.logger.error(f"no se pudo obtener la conexion: {e}")
            raise
            

            
            
    

    
