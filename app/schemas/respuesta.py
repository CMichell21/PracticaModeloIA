from pydantic import BaseModel,Field
from typing import Optional, Annotated

class Respuesta(BaseModel):
    codigoMensaje = str=Field(min_length=1, max_length=3)
    descripcionMensaje= str=Field(min_length=1, max_length=200)
    iguales = str=Field(min_length=1, max_length=2)
    sugerencia= Optional[str]=Field(
        default=None,
        min_length=1,
        max_length=1,
    )
    similitud= Annotated[int, Field(ge=1, le=100)]
