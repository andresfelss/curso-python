class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return self.nombre + other.nombre   # El metodo de suma me concatena los nombre pero puede hacer lo que yo quiera

    def __sub__(self, other):
        return self.edad - other.edad

# obj1 +obj2
# es igual a  obj1.__add__(obj2)

persona1 = Persona('Juan', 10)
persona2 = Persona('Carlos', 5)

print(persona1 + persona2)  # Me concatena los nombres
print(persona1 - persona2)   #Me resta las edades
