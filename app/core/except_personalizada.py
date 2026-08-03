class ServicioNoDisponible(Exception):

    def __init__(self,codigo,mensaje,usuario,metodo,clase):
        self.codigo=codigo
        self.mensaje=mensaje
        self.usuario=usuario
        self.metodo=metodo
        self.clase=clase
        super().__init__(mensaje)

class ErrorDatosDeEntrada(Exception):

    def __init__(self,codigo,mensaje,metodo,clase):
        self.codigo=codigo
        self.mensaje=mensaje
        self.metodo=metodo
        self.clase=clase
        super().__init__(mensaje)