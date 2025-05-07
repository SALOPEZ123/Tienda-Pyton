
import mysql.connector
def conectar(consulta_SQL):    
    config = {
'user': 'ujpz0l3osmj52tcx',
'password': 'oRLA3lQY1vIGFA583jSk',
'host': 'bmwxaqnthyefgx6jpifw-mysql.services.clever-cloud.com',
'database': 'bmwxaqnthyefgx6jpifw',
'raise_on_warnings': True
}

    try:
        conexion = mysql.connector.connect(**config)
        print("Conexión exitosa a la base de datos.")

        consulta = conexion.cursor()

        consulta.execute(consulta_SQL)

        resultado = consulta.fetchall()

        return resultado

    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
