# Decoradores 

def funcion_decoradora(funcion_parametro):

    def funcion_interior():

        # Acciones adiconales que decoran 

        print("Vamos a realizar un calculo")

        funcion_parametro()

        print("Hemos terminado el calculo")

    return funcion_interior

@funcion_decoradora #Aqui se llama a la funcion decoradora y hata lo que esta dentro de dicha funcion al hacer la funcion suma
def suma(): 

    print(15+20)

@funcion_decoradora
def resta():

    print(30-10)


suma()
resta()



