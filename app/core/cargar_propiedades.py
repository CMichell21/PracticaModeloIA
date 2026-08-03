import os
from dotenv import load_dotenv
from app.core.logger import getLogger
from app.core.logger import getLogger

class CargarPropiedades:

    logger = getLogger()
    
    def __init__(self,file=".env"):
        load_dotenv(file)

    def obtener_propiedades(self,parametro):
        
        value= os.getenv(parametro)

        if value is None or value.strip() == "":
            self.logger.error(f"no se pudo obtener el parametro: {parametro}") 
            raise ValueError(f"no se pudo obtner el parametro{parametro}")             
       
        return value.strip()

    



   
    


  