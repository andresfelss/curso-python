from NumerosIdenticosException import NumerosIdenticosException
a = 10
b = 10
r = None
try:
    r = a/b
    if a == b:
        raise NumerosIdenticosException('NUMEROS IDENTICOS')  # raise se utiliza para arrojar cualquier tipo de excepcion
except ZeroDivisionError as e:
    print(e)
except TypeError as te:
    print(f'Error de tipo: {te}')
except Exception as e:  # LA MAS GENERALLAS ABARCA A TODAS
    print(e)
else:   #solo si no se cumple la excepcion
    print('No se arrojo ninguna excepcion')
finally: # siempre se va a ejecutar SIEMPRE
    print('ejecuto finally')
print(r)
print('continuamos...')