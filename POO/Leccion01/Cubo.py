class Cubo:
    """
    Clase para calcular el volumen de un cubo

    """
    def __init__(self, alto, ancho ,profundidad):
        self.alto = alto
        self.ancho = ancho
        self.profundidad = profundidad
    def calcular_volumen(self):
        return self.alto*self.ancho*self.profundidad

w = int(input('Proporciona el ancho: '))
h = int(input('Proporciona el alto: '))
z = int(input('Proporciona lo profundo: '))

cubo1 = Cubo(h,w,z)
print(f'Volumen Cubo: {cubo1.calcular_volumen()} [m^3]')
