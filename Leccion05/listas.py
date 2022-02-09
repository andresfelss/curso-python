# Lista pueden tener diferentes tipos de variables
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']

print(nombres[0:3])

#acceder a los elementos inversa

print(nombres[-1]) #ultimo elemento

print(nombres[:3]) #ir del inicio de nuestra lista hasta el indice sin inculirlo

print(nombres[1:]) # ir desde el indice indicado hasta el final

nombres[3] = 'Andres' #modificando el valor del indice 3

#para iterar
for nombre in nombres:
    print(nombre)


#preguntar el largo de una lista

print(len(nombres)) # cantidad de elementos que tiene una lista

#agregar un elemento en nuestra lista
nombres.append('Lorenzo')
print(nombres)

# insertar un elemento en un indice en especifico
nombres.insert(1, 'Fary') # el indice 1 se inserta Fary y los demas se mueven hacia la derecha
print(nombres)
nombres.remove('Andres')
print(nombres)

#remover el ultimo valor agregado
nombres.pop()
print(nombres)

#eliminar un indice
del nombres[0]
print(nombres)

#limpiar todos los elementos de nuestra lista
nombres.clear()
print(nombres)

# borrar la lista por completo
del nombres
