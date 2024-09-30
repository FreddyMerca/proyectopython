import re

nombre_1="Freddy Mercado"
nombre_2="a16596091"
nombre_3="Sandra Cupajita"
nombre_4="19596091"
nombre_5="Lorena Leguizamo"
nombre_6="Sandra Leguizamo"

if re.match("\d", nombre_4): #Ignora mayusculas
    print("nombre Encontrado")
else:
    print("Nombre no encontrado")