def divide ():

    try:
        op1=float(input("Digite un numero: "))
        op2=float(input("Digite un numero: "))

        print("La diivision es " + str(op1/op2))
    except ValueError:
        print("Valor introducido erroneo")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    finally:
        #No importa que ocurra, se ejecuta siempre
        print("calculo Finalizado") 

divide()
