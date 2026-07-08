from pydantic import BaseModel, Field, field_validator
from typing import Optional, Annotated

class Peticion(BaseModel):
    aplicacion:str=Field(max_length=20) #
    servicio:Annotated[int, Field(ge=1,le=9999)]
    usuario:Optional[str]= Field(
        default=None,
        min_length=1,
        max_length=30
    )
    terminal:Optional[str]= Field(
        default=None,
        min_length=1,
        max_length=30
    )
    textoA:str=Field(min_length=1, max_length=32000)
    textoB:str=Field(min_length=1,max_length=32000)

    
class CompararPeticion(BaseModel):
    peticion:Peticion