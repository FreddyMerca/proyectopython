nombreUsuario=input("Introduce Nombre de Usuario: ")

print("El nombre de usuario es: ", nombreUsuario.upper())
print("El nombre de usuario es: ", nombreUsuario.lower())
print("El nombre de usuario es: ", nombreUsuario.capitalize())

edad=input("Introduce la edad: ")

while(edad.isdigit()==False):
    print("Por favor introduce un numero")

    edad=input("Introduce la edad: ")

if (int(edad)<18):

    print("No puede pasar")

else:
    print("puede pasar")





