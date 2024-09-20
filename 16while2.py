edad=int(input("introduce edad: "))

while edad<0 or edad>100:
    print("edad negatva, errada. Vuelve a intentar")
    edad=int(input("introduce edad: "))

print("Edad " + str(edad))

if edad > 18: 
    print("Edad Correcta, puedes continuar")
else:
    print("Menor de Edad")

