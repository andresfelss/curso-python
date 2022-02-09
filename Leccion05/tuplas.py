
# Tuplas

frutas = ('Naranjas', 'Platano', 'Guayabas')
# No podemos agregar modificar o eliminar elementos
print(len(frutas)) # cantidad de elementos de un tupla

#acceder a un elemento
print(frutas[0])  # igual que a las listas

print(frutas[0:1]) #  si solamente tiene un elemento es el valor y  la coma

for fruta in frutas:
    print(fruta, end = ' ') # cambiando el esapacio /n salto de linea por espacio

# frutas[0] = 'Pera' No se puede
# convertir una tupla a auna lista

list(frutas)




