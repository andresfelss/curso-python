
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creacion Objeto Cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(2, 'rojo')
print(cuadrado1)
print(cuadrado1.calcular_area())


print('Creacion Objeto Rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(ancho=5, alto=2, color='Verde')
print(rectangulo1)
print(rectangulo1.calcular_area())



#print(Cuadrado.mro()) # la forma u orden en que se manda a llamar la resolucion de nuestro problema
