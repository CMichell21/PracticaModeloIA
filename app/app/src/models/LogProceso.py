from sqlalchemy import Column, String,Integer, ForeignKey,Date

class LogProcesso():
    __tablesname__:"COMLPE"

    Id_LogProceso=Column(Integer,primary_key=True,nullable=False)
    Fecha=Column(Date,nullable=False)
    Tipo=Column(String(15), nullable=False)
    Mensaje=Column(String(300, nullable=True))
    Usuario=Column(String(30),nullable=False)
    Metodo=Column(String(300),nullable=False)
