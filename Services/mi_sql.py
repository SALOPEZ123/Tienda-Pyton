import mysql.connector

def conectar(consulta_SQL, parametros=None):
    config = {
        'user': 'ujpz0l3osmj52tcx',
        'password': 'oRLA3lQY1vIGFA583jSk',
        'host': 'bmwxaqnthyefgx6jpifw-mysql.services.clever-cloud.com',
        'database': 'bmwxaqnthyefgx6jpifw',
        'raise_on_warnings': True
    }

    try:
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor()

        if parametros:
            cursor.execute(consulta_SQL, parametros)
        else:
            cursor.execute(consulta_SQL)

        # Verifica si la consulta es SELECT
        if consulta_SQL.strip().lower().startswith("select"):
            resultados = cursor.fetchall()
            conexion.close()
            return resultados
        else:
            conexion.commit()
            conexion.close()
            return True  # indicar que fue exitoso

    except mysql.connector.Error as err:
        print(f"Error al conectar o ejecutar consulta: {err}")
        return None
