from sqlalchemy import Column, String,Integer, ForeignKey,Date

class LogProcesso():
    __tablesname__:"COMLPE"
    Id_LogPeticion=Column(Integer,primary_Key=True)
    Id_LogProceso=Column(Integer,ForeignKey("COMLPR.Id_LogProceso"),nullable=False)
    Fecha=Column(Date,nullable=False)
    Peticion=Column(String(1000),nullable=False)
    Respuesta=Column(String(1000),nullable=False)
