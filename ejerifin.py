print("Asignaturas")
opcion=(input("Escriba la asignatura: "))

asig=opcion.lower()

if asig in ("informatica", "electronica", "ambiental", "comunicacion"):
    print("asignatura " + asig)
else:
    print("Asignatura no contenplada")



