
try:
    archivo = open('Prueba.txt','w')
    archivo.write('Agregaos informacion al archivo\n')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()   # cuando se cierra no se puede trabajar mas con ese archivo
