from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Session

Base=declarative_base()

class Servicio(Base):
    #Teniendo en cuenta que se entran varios servicios
    #se agrega esta tabla para poder almacenar todos los servicios disponibles
    
    __tablesname__= "COMSER"

    id_servicio=Column(int, primary_Key=True)
    nombre_servicio=Column(str(500), nullable=False)
