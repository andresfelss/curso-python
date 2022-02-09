from usuario import Usuario
from usuario_dao import UsuarioDAO
from logger_base import log
option = None
while option != 5:
    print('Opciones: ')
    print('1. Listar Usuarios')
    print('2. Agregar usuario')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')
    option = int(input('Escribe tu opcion (1-5): '))
    if option == 1:
        usuarios = UsuarioDAO.seleccionar()
        for ususario in usuarios:
            log.info(ususario)
    elif option == 2:
        username_var = input('Escribe el username: ')
        password_var = input('Escribe el password')
        usuario = Usuario(username=username_var, password=password_var)
        usuarios_insertados = UsuarioDAO.insertar(usuario)
        log.info(f'Usuarios insertados: {usuarios_insertados}')
    elif option == 3:
        id_usuario_var = int(input('Escribe el id a modifica: '))
        username_var = input('Escribe el nuevo username: ')
        password_var = input('Escribe el nuevo password: ')
        usuario = Usuario(id_usuario = id_usuario_var, username=username_var, password=password_var)
        usuarios_modificados = UsuarioDAO.actualizar(usuario)
        log.info(f'Usuarios actualizados: {usuarios_modificados}')
    elif option == 4:
        id_usuario_var = int(input('Escribe el id a eliminar: '))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuarios_eliminados = UsuarioDAO.eliminar(usuario)
        log.info(f'Usuarios eliminados: {usuarios_eliminados}')
        
        
else:
    log.info('Salimos del programa...')