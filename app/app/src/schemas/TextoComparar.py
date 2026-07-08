from pydantic import BaseModel, Field, field_validator
from typing import Optional, Literal

class TextoComparar(BaseModel):
    textoA:str=Field(min_length=1,max_length=32000)
    textoB:str=Field(min_length=1, max_length=32000)
