
# obtener el factorial la funcion se llama a ella misma

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

resultado = factorial(5) 

print(resultado)