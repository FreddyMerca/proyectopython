#Practica Expresions Regualres

import re #Libreria para expresiones regulares

cadena="Cantidad de Expresiones regulares Python, el cual es un lenguaje de expresiones sencillas"

textoBuscar="Python"
textoEncontrado=re.search(textoBuscar, cadena)

print(textoEncontrado.start()) #Metodo Start muestra el numero de caracter donde inicia el texto
print(textoEncontrado.end())
print(textoEncontrado.span()) #donde inicia donde termina en una tupla

