
#no mantiene un orden, no admite elementos duplicados (no tienen indice )

planetas = {'Marte', 'Jupiter', 'Venus'}

'Marte' in planetas # preguntar si Marte esta en planetas

# Para agregar un elemento
planetas.add('Tierra')

# no se puede agregar dos elementos iguales

#eliminar elementos
planetas.remove('Tierra') # da error si no esta
planetas.discard('Tierra') # para eliminar un elemento sin arrojar error si es que no esta el elemento

planetas.clear(planetas) # para borrar todos los elementos
del planetas 



