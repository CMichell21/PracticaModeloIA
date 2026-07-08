from app.src.models.ActividadModel import ActividadModel
from fastapi import HTTPException
class ActividadService:
   
   def __init__(self):
      self.actividad= [
         ActividadModel(1,"python", "Pendiente"),
         ActividadModel(2,"vamos","En Proceso"), 
         ActividadModel(3,"probar", "Terminado")]
   

   def listarActividades(self, id:int ):   
      for actividad in self.actividad:
         if id==actividad.id :
            mostrarActividad= actividad 
            return mostrarActividad
      
      raise HTTPException( status_code=404,
                          detail=f"No existe la actividad con id {id}" )
   
   def agregarActividad (self, id:int,nombre:str,estado:str):
      for actividad in self.actividad:
         if id==actividad.id:
            raise HTTPException( status_code=404,
                          detail=f"No se puede agregar la actividad {id} porque ya existe" )
      self.actividad.append(ActividadModel(id,nombre,estado))
      return {"mensaje": "Actividad agregada con éxito"}

   def editarActividad (self,id:int,nombre=str, estado=str):
      for i in self.actividad:
         if id==i.id:
            i.nombre=nombre
            i.estado=estado
            return {"mensaje": "Actividad actualizada"}
      
      raise HTTPException( status_code=404,
                          detail=f"No existe la actividad con id {id}" )
            
            

   def eliminarActividad (self,id:int):
      for i in self.actividad:
         if i.id == id:
            self.actividad.remove(i)
            return {"mensaje":"Actividad eliminada"}
         
      raise HTTPException( status_code=404,
                          detail=f"No existe la actividad con id {id}" )
       
            