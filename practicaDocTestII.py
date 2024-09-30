import math

def raizCuadrada(listaNumeros):

    """"Esat funcion devuelve una lista con la raiz cuadrada de los elementos
    numericos pasados por parametros en una lista
    >>> lista=[]
    >>> for i in [4,9,16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    >>> [2.0, 3.0, 4.0]        
       
    """

    return[math.sqrt(n) for n in listaNumeros]

#print(raizCuadrado([9,16, 25, 36]))


import doctest
doctest.testmod()