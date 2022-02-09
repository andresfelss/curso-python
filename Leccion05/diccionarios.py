
# Key : values

dic = {
    'IDE' : 'Integrated Development Enviroment',
    'OOP' : 'objecto oriented progamming',
    'DBMS' : 'Database Management System'
}
# no tenemos indices

#print(dic['IDE'])

#print(dic.get('OOP'))
#MODIFICAR
dic['IDE'] = 'cambiado'
#print(dic)

#como recorrer los elementos de un dic
for termino, valor in dic.items():
    print(termino, valor)

for termino in dic.keys():
    print(termino)

for valor in dic.values():
    print(valor)

#comprobar existencia de algun elemento

print('IDE' in dic)


# agregar un elemento
dic['PK'] = 'primary key'
#print(dic)

#ELEIMINAR UN ELEMENTO
dic.pop('PK')

# eliminar todos los elementos
dic.clear()

del dic

