
# el * es que no sabemos el numero de lo que haya y lo convierte a tupla
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listarNombres('Juan', 'Karla', 'maria')
listarNombres('Andres','Angie')



