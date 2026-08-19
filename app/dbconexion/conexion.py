import unittest
from unittest.mock import patch, MagicMock

from app... import ConexionSql


class TestConexionSql(unittest.TestCase):

    @patch("app...conexion_sql.pymssql.connect")
    def test_conectar(self, mock_connect):

        conexion_falsa = MagicMock()

        mock_connect.return_value = conexion_falsa

        conexion = ConexionSql()

        resultado = conexion.conectar(
            url_ip="localhost",
            port=1433,
            usuario="usuario_test",
            password="password_test",
            db="BD_TEST",
            time_conection=10,
            time_read=5
        )

        self.assertEqual(resultado[0], conexion_falsa)
        self.assertEqual(resultado[1], "conectar")
        self.assertEqual(resultado[2], "ConexionSql")

        mock_connect.assert_called_once_with(
            server="localhost",
            port=1433,
            user="usuario_test",
            password="password_test",
            database="BD_TEST",
            login_timeout=10,
            timeout=5
        )


if __name__ == "__main__":
    unittest.main()
    


            
            
    

    
