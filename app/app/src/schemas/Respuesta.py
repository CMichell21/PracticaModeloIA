from pydantic import BaseModel, Field, field_validator
from typing import Optional, Literal

class Respuesta(BaseModel):
    codigoMensaje: str=Field(min_length=1,max_length=3)
    descripcionMensaje: str=Field(min_length=1,max_length=200)
    iguales: Literal["si","no"]
    sugerencia: Optional[Literal["A","I","R"]]=None
    similitud: int=Field(ge=0, le=100)

    @field_validator("similitud")
    @classmethod
    def validar_similitud(cls, v: int) -> int:
        if len(str(abs(v))) > 3:
            raise ValueError("cifra inconsistente")
        return v
