# ABC = Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo ancho: {ancho}')
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo alto: {alto}')
            print()
    # Metodo get y set
    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo alto: {alto}')

    def __str__(self):
        return f'Alto: {self._alto}\nAncho: {self._ancho}'

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False

    @abstractmethod   #indicamos que es un metodo abstracto, no se pueden crear obejetos de clases abstractas
    def calcular_area(self):
        pass