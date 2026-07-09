import pandas as pd
import json

from app.src.schemas.TextoComparar import TextoComparar
from app.modeloIA1.modeloIA import modeloIA

df = pd.read_excel("datos.xlsx")

resultado = []

modelo = modeloIA()

for _, fila in df.iterrows():

    textos = TextoComparar(
        textoA=fila["Despliegue_incoming"],
        textoB=fila["Despliegue_banco"]
    )

    objeto = modelo(textos, 0.8)

    resultado.append(objeto)

print(resultado)

with open("resultado.json", "w", encoding="utf-8") as archivo:
    json.dump(resultado, archivo, indent=4, ensure_ascii=False)

print("Archivo JSON generado correctamente.")
