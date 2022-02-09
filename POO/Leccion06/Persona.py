
class Persona:
    contador_perosnas = 0

    @classmethod

    def generar_siguiente_valor(cls):
        cls.contador_perosnas +=1
        return cls.contador_perosnas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'

persona1 = Persona('Andres', 21)
print(persona1)
persona2 = Persona('Karla', 5)
print(persona2)
print('Valor contador personas: ', Persona.contador_perosnas)
