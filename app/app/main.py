from app.dbConexion.Conexion import Conexion

def main():
    try:
        conexion = Conexion()

        conn = conexion.obtenerConexion()

        print(" Conexión exitosa a MySQL")

        # Prueba rápida de consulta
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")

        resultado = cursor.fetchone()

        print("Versión MySQL:", resultado[0])

        cursor.close()
        conn.close()

        print(" Conexión cerrada")

    except Exception as e:
        print(" Error:", e)


if __name__ == "__main__":
    main()
