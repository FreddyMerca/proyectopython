print("Programa becas 2024")
dist_uni=int(input("Distancia Universidad: "))
print(dist_uni)

num_herma=int(input("numero hermanos: "))
print(num_herma)

salario=int(input("Salario: "))

if dist_uni>40 and num_herma>2 or salario<=1300000:
    print("Derecho a beca")
else:
    print("no hay derecho")
    