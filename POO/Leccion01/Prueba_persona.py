
from get_set import persona


print('Creacion de objetos'.center(50, '-'))

persona1 = persona('Andres', 'Perez', 21)
persona1.mostrar_detalle() # se ejecuta el codigo del modulo importado

print('Eliminacion de objetos'.center(50, '-'))

del persona1 # es raro encontrar esto


