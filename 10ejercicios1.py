num1=int(input("Ingrese numero 1: "))
num2=int(input("Ingrese numero 2: "))

def DevuelveMax(n1, n2):
    if n1>n2:
        print (n1)
    elif n2>n1:
        print (n2)
    else:
        print ("Iguales")

DevuelveMax(num1, num2)