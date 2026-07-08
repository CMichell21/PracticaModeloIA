from dotenv import load_dotenv
import os

load_dotenv()
class Conexion:
    
    try:
        conexion = "el conector dependiendo del gestor a tratar".connect(
            DBHOST=os.getenv("DBHOST"),
            DBPORT=os.getenv("DBPORT"),
            DBNAME=os.getenv("DBNAME"),
            DBUSER=os.getenv("BDUSER"),
            PASSWORD=os.getenv("PASSWORD"),
            API_KEY= os.getenv("APIKEY")
        )
        print("Conexion exitosa")
    except "". Error as e:
        print("no se pudo conectar, e")
    finally:
        if 'conexion' in locals():
            conexion.close()