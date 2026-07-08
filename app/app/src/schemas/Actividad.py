from pydantic import BaseModel
from typing import Optional

class Mensaje(BaseModel):
    mensaje:str

class Actividad(BaseModel):
    id:int
    nombre:str
    estado:str


class ActividadActualizar(BaseModel):
    nombre:Optional[str]=None
    estado:Optional[str]=None
