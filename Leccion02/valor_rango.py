
a = int(input("Ingrese el valor: "))

ValorMin = 0
ValorMax = 5

dentroRango = (a >= ValorMin) and (a <= ValorMax)

if dentroRango:
    print(f'el valor {a} esta dentro del rango')
else:
    print(f'el valor {a} esta fuera del rango')
