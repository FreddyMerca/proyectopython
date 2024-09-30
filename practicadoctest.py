def compruebaMail(mailUsuario):

    """"Esta funcion valida y evalua si un mail esta correcto, si tiene una @ esta correcto, 
    si tiene mas de una @ esta incorrecto y si esta al final esta incorrecto
    >>> compruebaMail('frmercado@emcali.com.co')
    True

    >>>compruebaMail(frmercadoemcali.com.co@)
    False

    >>>compruebaMail(frmercado@emcali.com@.co)
    False

    
    
    """

    arroba=mailUsuario.count('@')

    if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
        return False

    else:
        True
    

import doctest
doctest.testmod()