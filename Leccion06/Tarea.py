
def suma_variable(*valores):

    for i in valores:
        i +=  i
    return i

print(suma_variable(1,2,3,5))

def producto(*args):
    p = 1
    for i in args:
        p = p*i
    return p

print(producto(1,1,5,2,2))

# dos astericos ara recibir un diccionario
def listarTerminos(**terminos):
    for llave,valor in terminos.items():
        print(f'{llave} : {valor}')

listarTerminos(IDE  = 'LO QUE SEA' , pkk = 'dasd')


# CON LISTAS

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombre = ['Juan', 'carla']

desplegarNombres(nombre)

