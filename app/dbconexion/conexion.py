import pymssql
import time
from app.core.logger import getLogger
from app.core.excepciones.error_conexion_bd import ErrorConexionBD

class ConexionSql:

    def __init__(self):
        self.logger=getLogger(__name__)

    def conectar(self, url_ip, port, usuario, password, db, time_conection, time_read):

        tiempo_inicial=time.perf_counter()

        try:
            self.logger.info("obteniendo conexion de la base de datos")

            conn= pymssql.connect(
                server=url_ip,
                port=port,
                user=usuario,
                password=password,
                database=db,
                login_timeout=time_conection,
                timeout=time_read
            )

            self.logger.info("conexion exitosa")
            
            conexion=[conn,"conectar",self.__class__.__name__]
            return conexion

        except Exception as error:
            self.logger.error(f"no se pudo obtener la conexion: {error}")
                
            raise ErrorConexionBD("012","No se pudo realizar la operación")

        finally:

            tiempo_final=time.perf_counter()
            tiempo_total=tiempo_final-tiempo_inicial
            self.logger.info(f"tiempo maximo de conexion esperado:{time_conection}, tiempo duracion:{tiempo_total} ")


    
    def desconectar(self, conn):

        try:
            if conn is not None:
                conn.close()
                self.logger.info("conexion cerrada exitosamente")

        except Exception as error:

            self.logger.error(f"no se pudo cerrar la conexion{error}")
            
    

    


            
            
    

    
