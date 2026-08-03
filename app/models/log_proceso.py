from datetime import datetime
class LogProceso:

    def __init__(self, 
                 uuid:str, 
                 tipo_log:str,
                 mensaje:str,
                 usuario:str,
                 metodo:str,
                 clase:str,
                 estado:str ):

        self.uuid=uuid
        self.tipo_log=tipo_log
        self.mensaje=mensaje
        self.usuario=usuario
        self.metodo=metodo
        self.clase=clase
        self.estado=estado