import re

nombre_1="Freddy Mercado"
Nombre_2="Lorena Mercado"
nombre_3="Sandra Cupajita"
nombre_4="Freddy Tello"
nombre_5="Lorena Leguizamo"
nombre_6="Sandra Leguizamo"

if re.match("Sandra", nombre_3, re.IGNORECASE): #Ignora mayusculas
    print("nombre Encontrado")
else:
    print("Nombre no encontrado")


