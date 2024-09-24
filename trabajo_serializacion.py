import pickle

#lista_nombres=["Freddy", "Liliana",  "Valery", "Karen"]

#fichero_binario=open("lista_nombres", "wb") #escritura binaria

#pickle.dump(lista_nombres, fichero_binario)

#fichero_binario.close()

#del (fichero_binario)

#Asi se creo el fichero

fichero=open("lista_nombres", "rb") #leer binario
lista=pickle.load(fichero)

print(lista)


