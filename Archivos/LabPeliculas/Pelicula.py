
class Pelicula:
    contador_pelicula = 0
    def __init__(self, nombre):
        self._nombre = nombre
        Pelicula.contador_pelicula += 1
        self.id_peli = Pelicula.contador_pelicula

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'{self.id_peli}.{self._nombre}\n'
