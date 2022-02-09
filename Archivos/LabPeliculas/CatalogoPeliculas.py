import os

from Pelicula import Pelicula


class CatalogoPeliculas:
    contador_peliculas = 0
    ruta_archivo = 'peliculas.txt'
    @classmethod
    def agregar_pelicula(cls, pelicula):
        cls.contador_peliculas += 1
        id_pelicula = cls.contador_peliculas
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{id_pelicula}.{pelicula.nombre}\n')
    @classmethod
    def listar_pelicula(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print('Catalogo Peliculas'.center(50, '-'))
            print(archivo.read())
    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo Eliminado. {cls.ruta_archivo}')


pelicula1 = Pelicula('High School musical')
pelicula2 = Pelicula('Iron man')
CatalogoPeliculas.agregar_pelicula(pelicula1)
