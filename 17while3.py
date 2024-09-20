import math

print("Calculo raiz")
num=int(input("introduce un numero: "))

intentos=0

while num<0:
    print("No se puede hallar la raiz de un numero negativo")
          
    if intentos==2:
            print("Demasiados Intentos")
            break
    num=int(input("introduce un numero: "))
    if num<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(num)
    print("la raiz es: " + str(solucion))



