#Practica Expresions Regualres

import re #Libreria para expresiones regulares

cadena="Cantidad de Expresiones regulares Python, el cual es un lenguaje de expresiones sencillas. Por eso Python es tan usado"

textoBuscar="Python"
print(len(re.findall(textoBuscar, cadena))) #Devuelve todos los textos en una lista 
