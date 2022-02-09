#with open('Prueba.txt', 'r') as archivo:
from ManejoArchivos import ManejoArchivos

with ManejoArchivos('Prueba.txt') as archivo:
    print(archivo.read())