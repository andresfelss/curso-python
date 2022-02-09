from Color import Color
from FiguraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica,Color):
    def __init__(self, lado, color):
     # super().__init__(lado)
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    def calcular_area(self):
         return f'Area: {self.alto * self.ancho}'
    def __str__(self):
        return f'El cuadrado tiene las siguientes caracteristicas\n{FiguraGeometrica.__str__(self)}\n{Color.__str__(self)}'
