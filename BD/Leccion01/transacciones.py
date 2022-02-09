import psycopg2 as bd

conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:  # ABRIR NUESTRA CONEXXION
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
            valores = ('franciso', 'Ramirez', 'pacho@email.com')
            cursor.execute(sentencia, valores)

            # sentencia = 'UPDATE persona SET nombre = %s, apellido=%s, email = %s WHERE id_persona = %s'
            # valores = ('Juan', 'aldana','juanaldana@email.com',1)
            # cursor.execute(sentencia,valores)

            # sentencia = 'DELETE FROM persona WHERE id_persona = 12'
            # cursor.execute(sentencia)
            # CON WITH NO ES NECESARIO EL USO DEL COMMIT
            # si falla tambien se hace el rollback automatico
except Exception as e:
    print(f'an error in the transaction occurs: {e}')
finally:
    conexion.close()  # close the connexion with the database
    print('Transactions Ends')
