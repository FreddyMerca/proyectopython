import re

nombre_1="Freddy Mer17cado"
nombre_2="Marco Fidel Suarez"
nombre_3="Sandra Cup17ajita"
nombre_4="Marcell Merc17ado"
nombre_5="Lorena Leguizamo"
nombre_6="Sandra Leguizamo"

if re.search("17", nombre_3, re.IGNORECASE): #Ignora mayusculas
    print("nombre Encontrado")
else:
    print("Nombre no encontrado")