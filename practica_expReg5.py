#Practica Expresions Regualres

import re #Libreria para expresiones regulares

listaNombres=['frmercado@emcali.com.com',
              'massiel69@hotmail.com',
              'lulito131gmail.com',
              'alemartinezemcali.com.co',
              'freddy.mercado131gmail.com',
              ]

for elemento in listaNombres:
    if re.findall ('[@]', elemento): #Todos los que finalizan por esa cadena  y los imprime
        
        print(elemento)

