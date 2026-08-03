import os
from dotenv import load_dotenv
from app.core.logger import getLogger
from app.core.except_personalizada import ErrorConexionBD

class Config:

    logger = getLogger()
    
    def __init__(self,file=".env"):
        load_dotenv(file)
        self.DB_DRIVER= self.obtener_propiedades('NAME_CLASS')
        self.URL= self.obtener_propiedades('URL')
        self.DB_USER= self.obtener_propiedades('DB_USER')
        self.DB_PASSWORD= self.obtener_propiedades('DB_PASSWORD')
        self.DB_JAR= self.obtener_propiedades('ADDRES_DRIVER')
        self.AMBIENTE=self.obtener_propiedades('AMBIENTE')

    def obtener_propiedades(self,parametro):
        
        value= os.getenv(parametro)

        if value is None or value.strip() == "":
            raise ErrorConexionBD(f"no se pudo obtener el parametro{parametro}")             
       
        return value.strip()
    

config=Config()
    



   
    


  
    



   
    


  



   
    


  
