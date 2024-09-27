#def area_triangulo(base, altura):
  #  return (base * altura) / 2

# Solicitar al usuario que ingrese los valores
#base = float(input("Ingresa la base del triángulo: "))
#altura = float(input("Ingresa la altura del triángulo: "))

# Llamar a la función con los valores ingresados
#resultado = area_triangulo(base, altura)

# Mostrar el resultado
#print(f"El área del triángulo es: {resultado}")

area_triangulo=lambda base,altura:(base*altura)/2 #Sintaxis fuhciona anonima

base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))

resultado = area_triangulo(base, altura)
print(f"El área del triángulo es: {resultado}")


