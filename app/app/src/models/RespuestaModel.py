class Respuesta:
    def __init__(self, codigoMensaje:str, descripcionMensaje:int, iguales:str, 
                 sugerencia:str,similitud:str):
        self.codigo=codigoMensaje
        self.descripcion=descripcionMensaje
        self.iguales=iguales
        self.sugerencia=sugerencia
        self.similitud=similitud
    