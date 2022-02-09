
class Vehiculo:
    def __init__(self, _color, _ruedas):
        self._color = _color
        self._ruedas = _ruedas

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def ruedas(self):
        return self._ruedas

    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas

    def __str__(self):

        return f'Color:{self._color} \nRuedas: {self._ruedas} '


class coche(Vehiculo):

    def __init__(self, _color, _ruedas, velocidad):
        super().__init__(_color, _ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()}\nTipo: Auto\nVelocidad: {self.velocidad} '

class bicicleta(Vehiculo):

    def __init__(self, _color, _ruedas, tipo):
        super().__init__(_color, _ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'{super().__str__()}\nBicicleta tipo: {self.tipo}'



if __name__ == '__main__':
    vehiculo1  = bicicleta('Roja', 2, 'Montañismo')
   # print(vehiculo1)

    vehiculo2 = coche('Negro', 4, 100)
   # print(vehiculo2)

    vehiculo3 = Vehiculo('Azul', 2)
    print(vehiculo3)
    vehiculo3.ruedas = '10'
    print(vehiculo3)