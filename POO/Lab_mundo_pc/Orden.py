from Computadora import Computadora
from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Orden:
    contadorOrdenes = 0

    def __init__(self, computadoras):
        Orden.contadorOrdenes += 1
        self._idOrdenes = Orden.contadorOrdenes
        self._computadoras = computadoras

    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()
        return f'''
        Orden: {self._idOrdenes}
        Computadoras: {computadoras_str}
        '''


teclado1 = Teclado('Apple', 'USB')
raton1 = Raton('Ryzen', 'Blutu')
monitor = Monitor('DELL', '18 pulgadas')
computadora1 = Computadora('Lenovo', monitor, teclado1, raton1)
computadoras1 = [computadora1]
#print(orden1)

teclado2 = Teclado('AppleE', 'USB')
raton2 = Raton('RyzenE', 'Blutu')
monitor2 = Monitor('DELLE', '18 pulgadas')
computadora2 = Computadora('Gamer', monitor2, teclado2, raton2)
computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
#orden1.agregarComputadora(computadoras2)
#print(orden1)

computadora3 = Computadora('Andres', monitor2, teclado2, raton2)

orden2 = Orden(computadoras1)
print(orden2)

orden1.agregarComputadora(computadora3)

print(orden1)
print(computadoras1)

# orden2 = Orden(computadoras1)
# print(orden2)