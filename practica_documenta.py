from modulos import funciones_matematicas


class Areas:

    """Calcula el area de diferentes figuras geometricas"""

    def areaCuadrado(lado):

        """ Calcula el area de un cuadrado elevando el cuadrado al lado pasado por parametro""" #Documentacion

        return  "el area del cuadra es : " + str(lado * lado)

    def areaTriangulo (base, altura):

        """Calcula el area del triangulo"""

        return "El area del triangulo es : " + str((base * altura)/2)


help(funciones_matematicas)