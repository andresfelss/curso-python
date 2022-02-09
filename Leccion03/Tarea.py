Nota = float(input('Proporcione el valor: '))

if 9 <= Nota <= 10:
    calificacion = 'A'
elif 8 <= Nota < 9:
    calificacion = 'B'
elif 7 <= Nota < 8:
    calificacion = 'C'
elif 6 <= Nota < 7:
    calificacion = 'D'
elif 0 <= Nota < 6:
    calificacion = 'F'
else:
    calificacion = 'Valor desconocido'

print(f'{calificacion}')

