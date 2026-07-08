from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Servicio():
    #Teniendo en cuenta que se entran varios servicios
    #se agrega esta tabla para poder almacenar todos los servicios disponibles
    
    __tablesname__= "COMSER"

    id_servicio=Column(int, primary_Key=True)
    nombre_servicio=Column(str(500), nullable=False)
