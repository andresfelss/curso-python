
class MiClase:
    variable_clase = 'Valor variable clase'   # Valor de clase solo se asocian en la clase

    def __init__(self, varable_instancia):
        self.variable_instancia = varable_instancia

    @staticmethod
    def metodo_estatico(): # no recibe la palabra self
        print(MiClase.variable_clase)   # no pueden acceder a las variables de instancia

    @classmethod
    def metodo_clase(cls):              # cls parametro de la clase en si misma
        print(cls.variable_clase)  #para acceder a la variable de clase directamente

    def metodo_instancia(self):
        self.metodo_clase()  # podemos acceder a los metodos estaticos o de clase
        self.metodo_estatico()

 # para llamar el metodo estatico
MiClase.metodo_estatico() # asi
# para llamar el metodo de clase
MiClase.metodo_clase()

print(MiClase.variable_clase)

miclase1 = MiClase('Valor variable instancia')
print(miclase1.variable_instancia)
print(miclase1.variable_clase)  # Puedo acceder a la variable de clase y sera la misma y no esta vinculada a obj

MiClase.variable_clase2 = 'Valor variable clase 2' # creacion de variable de clase al vuelo en cualquier momento

miObjeto1 = MiClase('vi')

miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()