class persona:
        def __init__(self, nombre, apellido, edad):
            self._nombre = nombre
            self._apellido = apellido
            self._edad = edad
        @property #podaos seguir accediendo a nuestro metodo
        def nombre(self):
            return self._nombre

        @nombre.setter
        def nombre(self,nombre):
            self._nombre = nombre

        @property
        def apellido(self):
            return self._apellido
        @apellido.setter

        def apellido(self, apellido):
            self._apellido = apellido
        @property
        def edad(self):
            return self._edad
        @edad.setter
        def edad(self, edad):
            self._edad = edad

        def mostrar_detalle(self):
            print(f'persona: {self._nombre} {self._apellido} {self._edad}')

        def __del__(self):
            print(f'Persona: {self._nombre} {self._apellido} fue eliminado')

if __name__ == '__main__':
    persona1 = persona('Juan', 'Perez', 21)

    persona1.nombre
    print(persona1.nombre)

#para cambiar ese ateributo se usa lo de set
    persona1.nombre = 'Andres Felipe'

    print(persona1.nombre)



