
class Aritmetica:
    """
    Clase aritmetica para realizar las operaciones de sumar restar, etc

    """
    def __init__(self,operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    def restar(self):
        return self.operandoA - self.operandoB
    def multiplicar(self):
        return self.operandoA * self.operandoB
    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(5,3)  # Creo el objeto

print(aritmetica1.sumar()) # LLamo a la suma
print(aritmetica1.restar())
print(aritmetica1.multiplicar())
print(f'{aritmetica1.dividir():.2f}')  # El .2f es para mostar solo dos digitos

