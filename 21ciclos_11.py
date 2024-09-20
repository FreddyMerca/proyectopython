#Contar os caracteres de un String

nombre=str(input("Digite un texto: "))
contador=0

for i in nombre:

    if i==" ":
        continue
#Ignora el espacio y continua, no cuenta los espacios
    contador+=1
    
print(contador)
