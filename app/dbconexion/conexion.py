from unittest.mock import patch

import pytest

from app.infraestructura.conexion_sql import ConexionSql
from app.core.excepciones.error_conexion_bd import ErrorConexionBD


def test_conectar_error():

    conexion = ConexionSql()

    with patch(
        "app.infraestructura.conexion_sql.pymssql.connect"
    ) as mock_connect:

        mock_connect.side_effect = Exception(
            "Error de conexión"
        )

        with pytest.raises(ErrorConexionBD):
            conexion.conectar(
                url_ip="192.168.1.100",
                port=1433,
                usuario="usuario_test",
                password="password_test",
                db="BD_TEST",
                time_conection=10,
                time_read=20
            )


            
            
    

    
