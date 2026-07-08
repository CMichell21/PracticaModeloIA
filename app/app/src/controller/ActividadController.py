from app.src.services.ActividadService import ActividadService
from app.src.schemas.Actividad import Actividad, ActividadActualizar, Mensaje
from fastapi import FastAPI
import os
from dotenv import load_dotenv


app = FastAPI()
service=ActividadService()
load_dotenv()
API_KEY=os.environ.get('APIKEY')
 
@app.get("/actividad/{id}", response_model=Actividad)
def obtenerActividad(id:int):
    actividad= service.listarActividades(id)
    return Actividad(id=actividad.id,nombre=actividad.nombre, estado=actividad.estado)
   
    
@app.post("/actividad")
def agregarActividad(actividad:Actividad):
    return service.agregarActividad(actividad.id,actividad.nombre, actividad.estado) 
        
@app.put("/actividad/{id}")
def editarActividad(id:int,campoActualizar:ActividadActualizar):
    return service.editarActividad(id,campoActualizar.nombre,campoActualizar.estado)


@app.delete("/actividad/{id}")
def eliminarActividad(id:int):
    return service.eliminarActividad(id)
