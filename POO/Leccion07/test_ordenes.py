from Orden import Orden
from Producto import Producto

producto1 = Producto('Camisa', 100.00)
producto2 = Producto('Pantalon', 150.00)
producto3 = Producto('Calcetines', 50.00)
producto4 = Producto('Blusa', 60.66)
productos = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos)
print(orden1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)

print(orden1.calcular_total())
