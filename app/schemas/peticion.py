from pydantic import BaseModel, Field, ConfigDict
from typing import Optional,Annotated

class CuerpoPeticion(BaseModel):
    model_config = ConfigDict(extra="forbid")
    aplicacion:str=Field(min_length=1, max_length=20)
    servicio:Annotated[int, Field(ge=1, le=9999)]
    usuario:Optional[str]=Field(
        default="transformapi",
        min_length=1,
        max_length=30
        )
    terminal:Optional[str]=Field(
        min_length=1, 
        max_length=30
        )
    textoA:str=Field(min_length=12,max_length=32000)
    textoB:str=Field(min_length=12,max_length=32000)

class Peticion(BaseModel):
    
    model_config = ConfigDict(extra="forbid")
    peticion:CuerpoPeticion