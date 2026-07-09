from sqlalchemy import Column, ForeignKey,String,Integer
from sqlalchemy.orm import sessionmaker, declarative_base, Session

Base=declarative_base()
class Peticion(Base):
    #Esta tabla guarda las peticiones hechas por ek cliente
    __tablename__="COMPET"

    Id_peticion=Column(Integer, primary_key=True)
    Aplicacion=Column(String(20), nullable=False)
    Id_servicio=Column(Integer,ForeignKey("COMSER.Id_servicio"), nullable=False)
    Usuario=Column(String(30))
    Terminal=Column(String(30))
    TextoA=Column(String(32000), nullable=False)
    TextoB=Column(String(32000), nullable=False)
