#Practica Expresions Regualres

import re #Libreria para expresiones regulares

listaNombres=['Leonor Leguizamo',
              'Massiel Mercado',
              'Freddy Mercado',
              'Alejandro Martinez',
              'Freddy Ricardo Mercado',
              ]

for elemento in listaNombres:
    if re.findall ('Mercado$', elemento): #Todos los que finalizan por esa cadena  y los imprime
        
        print(elemento)

