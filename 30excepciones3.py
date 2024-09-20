def evaluaEdad(edad):

    if edad<0:
        raise TypeError("Edad Negatva ?")
    if edad<20:
        return "eres muy joven "
    elif edad<40:
        return "Alejo"
    elif edad<65:
        return "Zamudio"
    elif edad<100:
        return "Luis Vivas"
    
print(evaluaEdad(-15))

