from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Computadora:
    contadorComputadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras += 1
        self._idComputadora = Computadora.contadorComputadoras
        self._nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'''
        {self.nombre}: {self._idComputadora}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}      
        '''


if __name__ == '__main__':
    teclado1 = Teclado('Apple', 'USB')
    raton1 = Raton('Ryzen', 'Blutu')
    monitor = Monitor('DELL', '18 pulgadas')
    computadora1 = Computadora('Nora pc', monitor, teclado1, raton1)
    print(computadora1)

    teclado2 = Teclado('AppleE', 'USB')
    raton2 = Raton('RyzenE', 'Blutu')
    monitor2 = Monitor('DELLE', '18 pulgadas')
    computadora2 = Computadora('Pipe PC', monitor2, teclado2, raton2)
    print(computadora2)
