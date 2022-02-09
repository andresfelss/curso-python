archivo = open('Prueba.txt', 'r', encoding='utf8')  # r de read es el modo default ,a para append
# print(archivo.read())
# si ya se leyo no se puede volver a leer
# leer algunos caracteres
# print(archivo.read(5))  # se leen los primeros 5 caracteres

# leer lineas completas
# print(archivo.readline())

# iteras
# for linea in archivo:
#    print(linea)
# print(archivo.readlines()[1])

# abrimos un nuevo archivo

archivo2 = open('Copia.txt', 'a')
archivo2.write(archivo.read())

