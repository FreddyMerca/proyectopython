#Creacion de archivos desde python
from io import open 

archivo_texto=open("archiv.txt", "r+") #Lectura y escritura

#print(archivo_texto.readlines())

lista_texto=archivo_texto.readlines();
lista_texto[1]="Linea incluida desde el exterior\n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()




