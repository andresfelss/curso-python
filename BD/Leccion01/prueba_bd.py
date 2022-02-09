import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona los id persona a eliminar seaprados por coma:')
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)
            registros_eliminadoss = cursor.rowcount
            print(f'Registros actualizados: {registros_eliminadoss}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
