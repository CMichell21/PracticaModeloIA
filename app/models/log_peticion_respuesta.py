from datetime import datetime

class LogPeticionRespuesta:
    
    def __init__(self,
                 uuid:str,
                 pet_usuario:str,
                 res_api:str, 
                 fecha_peticion:datetime, 
                 fecha_respuesta:datetime
                 ):

        self.uuid=uuid         
        self.pet_usuario=pet_usuario
        self.res_api=res_api
        self.fecha_peticion=fecha_peticion
        self.fecha_respuesta=fecha_respuesta