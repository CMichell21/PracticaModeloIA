from app.models.log_proceso import LogProceso
from app.dbconexion.conexion import Conexion
from app.core.cargar_propiedades import CargarPropiedades
from app.core.logger import getLogger

class LogProcesoRepository:
    def __init__(self):
        self.conexion= Conexion()
        self.logger= getLogger(__name__)
        self.ambiente= CargarPropiedades()

    def insertar(self, log:LogProceso):

        try:
            conn=self.conexion.Conectar()

            sql=f"""
                   INSERT INTO 
                   {self.ambiente.obtener_propiedades('AMBIENTE')}USRLIB.TRALPR(
                   UUID, TIPO_LOG, MENSAJE, USUARIO, METODO, CLASE, ESTADO) 
                   VALUES (?,?,?,?,?,?,?)
                   """

            cursor=conn.cursor()

            cursor.execute(sql, (
                log.uuid,log.tipo_log, 
                log.mensaje, log.usuario, 
                log.metodo, log.clase, 
                log.estado)
                )
            
            conn.commit()
            self.logger.info("log registrado correctamente")

            cursor.close()
            conn.close()

        except Exception as e:
            self.logger.error(f"No se pudo insertar el log:{e}")
            raise 
        

        
    
    def consultarLog(self):

        conn= self.conexion.Conectar()
        try:
            sql=F"""
                SELECT * FROM {self.ambiente.obtener_propiedades('AMBIENTE')}USRLIB.TRALPR
            """     
            cursor= conn.cursor()
            
            cursor.execute(sql)
            cursor.close()
            conn.close()

        except Exception as e:
            self.logger.error(f"no se pudo ver la consulta{e}")
            raise e

           






