from sqlalchemy import Column, ForeignKey, Integer,String
from sqlalchemy.orm import sessionmaker, declarative_base, Session

Base=declarative_base()
class Respuesta(Base):
    #esta tabla guarad las respuestas obtenidas por el sistema
    __tablesname__="COMRES"
    
    Id_respuesta=Column(Integer,primary_key=True)
    Id_peticion=Column(Integer, ForeignKey("COMPET.Id_peticion", ondelete="SET NULL"), nullable=False)
    codigo_mensaje=Column(String(3),nullable=False, nullable=False)
    Descripcion_mensaje=Column(String(200),nullable=False)
    Iguales=Column(String(2),nullable=False)
    Sugerencia=Column(String(1),nullale=True)
    Similitud=Column(Integer, nullable=False)

    
