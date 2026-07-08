from sqlalchemy import Column
from sqlalchemy.orm import sessionmaker, declarative_base, Session

class Peticion():
    #Esta tabla guarda las peticiones hechas por ek cliente
    __tablename__="PETCOM"

    Id_peticion=Column(int, primary_key=True)
    Aplicacion=Column(str(20), nullable=False)
    Servicio=Column(int, nullable=False)
    Usuario=Column(str(30))
    Terminal=Column(str(30))
    TextoA=Column(str(32000), nullable=False)
    TextoB=Column(str(32000), nullable=False)

