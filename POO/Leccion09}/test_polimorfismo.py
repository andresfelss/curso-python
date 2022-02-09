from Empleado import Empleado
from Gerente import Gerente

# ACA SE APLICA EL CONCEPTO DE POLIMORFISMO
def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))
    if isinstance(objeto,Gerente):  # se ejecuta si el objeto es de la clase gerente
        print(objeto.departamento)

empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Pedro', 6000, 'Sistemas')
imprimir_detalles(gerente)

