
edad = int(input('Proporciona tu edad: '))

if  0 <= edad < 10:
    print('La infancia es muy increible')
elif edad > 10 and edad <= 20:
    print('Muchos cambios y mucho estudio')
elif edad > 20 and edad <= 30:
    print('Amor y comienza el trabajo ... ')
else:
    print('Etapa de vida no reconocida')
