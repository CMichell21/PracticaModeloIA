from app.models.log_peticion_respuesta import LogPeticionRespuesta
from app.core.cargar_propiedades import CargarPropiedades
from app.dbconexion.conexion import Conexion
from app.core.logger import getLogger

class LogPeRepository:

    def __init__(self):
        self.logger=getLogger()
        self.conectar= Conexion()
        self.ambiente=CargarPropiedades()

    def insertar(self, log:LogPeticionRespuesta):
        try:
            conn= self.conectar.Conectar()

            sql= f"""
                INSERT INTO 
                {self.ambiente.obtener_propiedades('AMBIENTE')}USRLIB.TRALPE(UUID,PET_USUARIO,RES_API,FECHA_PETICION,FECHA_RESPUESTA) 
                VALUES (?,?,?,?,?) 
                """
            cursor= conn.cursor()
            
            cursor.execute(sql,( 
                log.uuid, 
                log.pet_usuario, 
                log.res_api, 
                log.fecha_peticion, 
                log.fecha_respuesta)
                )
            

            conn.commit()

            self.logger.info("log registrado correctamente")

            cursor.close()

            conn.close()

        except Exception as error:

            self.logger.error(f"No se pudo insertar el log {error}")
            raise

       

    def actualizar(self, log:LogPeticionRespuesta):
        try:
            conn= self.conectar.Conectar()

            cursor= conn.cursor()

            sql= F"""
                UPDATE {self.ambiente.obtener_propiedades('AMBIENTE')}USRLIB.TRALPE
                SET RES_API=?, FECHA_RESPUESTA=?
                WHERE UUID=?
                """
            
            cursor.execute(sql,(
                log.res_api, 
                log.fecha_respuesta,
                log.uuid
                ))
            
            conn.commit()

            cursor.close()
            conn.close()
            self.logger.info("actualizacion de log peticion y respuesta exitoso")

        except Exception as error:
            self.logger.error(f"no se pudo actualizar el log con uuid: {error}")
            raise 
            



