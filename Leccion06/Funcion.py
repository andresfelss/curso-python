
#para definir una funcion

def mi_funcion(nombre, apellido):

    print(nombre, apellido)


# La podeos reutilizar las veces que queramos.

# Paso de argumentos o parametros

mi_funcion('Andres', 'Perez')

# Palabra return

def sumar(a, b):
    return a + b

resultado = sumar(1,1)
print(resultado)


#valor por default

def sumar2(a = 0, b = 0):
    return a + b
# si no le das argumentos tomara los resultados por default

