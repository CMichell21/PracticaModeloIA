from fastapi import APIRouter, Depends, status, Request
from app.service.comparar_orquestador import CompararService
import json

router = APIRouter(prefix="/transformapi", tags=["Comparar"])

orquestador = CompararService()

@router.post("/comparar")
async def comparar (request: Request):
    peticion= await request.json()
    resultado= await orquestador.ejecutar_proceso(peticion)   

    return 
