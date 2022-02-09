# Programacion orientada a objetos
class Persona:
    def __init__(self,name, apellido, edad): # Agregar atributos a nuestra clase , metod dunder doblre guin bajo
        self.nombre = name
        self.apellido = apellido
        self.edad = edad
    # creacion de metodos
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido},{self.edad}')


persona1 = Persona('Andres', 'Perez', 21)
# PARA LLAMAR EL METODO
persona1.mostrar_detalle()
# otra forma mismo resultado
Persona.mostrar_detalle(persona1)
# se crea un nuevo atributo pero no se comparte con los demas objetos
persona1.telefono = '3128056643'

# print(persona1.nombre)   #clase.atributo
# print(persona1.apellido)
# print(persona1.edad)

persona2 = Persona('Nora', 'Arzuaga', 20)

persona2.mostrar_detalle()
# Modificar atributos de un objeto
# persona1.nombre = 'Miguel'
# persona2.apellido = 'Carrillo' # se modifica el atributo seleccionado

#  Metodos de instancia






