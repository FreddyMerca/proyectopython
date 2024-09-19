#Funciona que devuelve ciudades

def devuelve_ciudad(*ciudades): #El * delante del elementos es indicarle
    #que va a recibir un numero indeterminado de elementos
    
    for elemento in ciudades:
        #for subElemento in elemento: 
        yield from elemento

ciudades_devueltas=devuelve_ciudad("Cali", "Bogota", "Medellin")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

