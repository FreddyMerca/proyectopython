#Practica Expresions Regualres

import re #Libreria para expresiones regulares

listaNombres=['Leonor Leguizamo',
              'Massiel Mercado',
              'Freddy Mercado',
              'Alejandro Martinez',
              'Freddy Ricardo Mercado',
              ]

for elemento in listaNombres:
    if re.findall ('^Freddy', elemento): #Todos los que inician por ese nombre y los imprime
        
        print(elemento)

