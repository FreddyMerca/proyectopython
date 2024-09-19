def pedir_numeros():
    # Inicializamos la variable para almacenar el número anterior
    numero_anterior = None
    
    while True:
        try:
            numero = int(input("Introduce un número: "))
            
            # Comprobamos si es la primera comparacion
            if numero_anterior is not None:
                if numero <= numero_anterior:
                    print(f"El número {numero} es menor o igual que el número anterior ({numero_anterior}). Fin del programa.")
                    break
            
            # Actualizamos el número anterior
            numero_anterior = numero
            
        except ValueError:
            print("Por favor, introduce un número entero válido.")

# Llamamos a la función
pedir_numeros()