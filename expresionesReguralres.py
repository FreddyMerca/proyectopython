#Practica Expresions Regualres

import re #Libreria para expresiones regulares

cadena="Cantidad de Expresiones regulares Python"

textoBuscar="Python"

if re.search(textoBuscar, cadena) is not None:

    print("Texto encontrado")

else: 
    print("Texto no encontrado")

    
