
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
a = 0
for i in tupla:
    if i < 5:
        lista.insert(a, i)
        a += 1

print(lista)