def suma(num1, num2):
	return num1+num2
#Suma dos numeros
def resta(num1, num2):
	return num1-num2
#Resta dos numeros
def multiplica(num1, num2):
	return num1*num2
#multiplica dos numeros
def divide(num1,num2):
	try:
		return num1/num2
	except ZeroDivisionError:
		print("No es posible dividir entre cero")
		return "Operacion erronea"

#divide dos numeros

#Excepcion para evitar conmando alfabetico en vez de numerico
while True:
	try:
		op1=(int(input("Introduce el primer número: ")))
		op2=(int(input("Introduce el segundo número: ")))
		break
	except ValueError:
		print ("No introdujo numero")

#Soliciita dos numeros
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")
 
if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")
