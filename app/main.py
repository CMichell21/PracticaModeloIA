import traceback
from fastapi import FastAPI, Request
from app.api.comparar import router
from fastapi.responses import JSONResponse
from app.core.except_personalizada import ServicioNoDisponible, ErrorDatosDeEntrada

app = FastAPI(
    title="transformapi",
    description="api para poder consumir un modelo de ia"
)
  
app.include_router(router)

##CAPTURAMOS LAS EXCEPCIONES Y LAS MANDAMOS AL CLIENTE
## excepciones handler

@app.exception_handler(ErrorDatosDeEntrada)
async def erros_datos_entrada(
    request:Request,
    dato:ErrorDatosDeEntrada):
    
    return JSONResponse(
        status_code=400,
        content={
            "codigo":dato.codigo,
            "mensaje": dato.mensaje
        }
    )


@app.exception_handler(ServicioNoDisponible)
async def servicio_no_disponible_handler(
    request:Request, 
    dato:ServicioNoDisponible):

    return JSONResponse(
        status_code=400,
        content={
            "codigo":dato.codigo,
            "mensaje":dato.mensaje
        }
    )

@app.exception_handler(Exception)
async def excepciones_generales(request:Request,dato):

    return JSONResponse(
        status_code=500,
        content={
            "codigo":500,
            "mensaje": "error interno del servidor"
        }
    )
