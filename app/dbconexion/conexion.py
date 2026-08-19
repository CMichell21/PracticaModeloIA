(.venv) PS C:\Users\ncarrillo\OneDrive - FICENSA\Documents\Transformapi> python -m unittest test.dbconexion.test_conexion_sql
E
======================================================================
ERROR: test_conectar (test.dbconexion.test_conexion_sql.TestConexionSql.test_conectar)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\ncarrillo\OneDrive - FICENSA\Documents\Transformapi\test\dbconexion\test_conexion_sql.py", line 17, in test_conectar
    resultado=conexion.conectar(
        server="localhost",
    ...<5 lines>...
        timeout=5
    )
TypeError: ConexionSql.conectar() got an unexpected keyword argument 'server'

----------------------------------------------------------------------
Ran 1 test in 0.002s

FAILED (errors=1)
(.venv) PS C:\Users\ncarrillo\OneDrive - FICENSA\Documents\Transformapi> 
    


            
            
    

    
