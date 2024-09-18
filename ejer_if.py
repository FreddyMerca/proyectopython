nota_alumn=int(input("Ingresa la nota: "))
def evaluacion(nota):
    examen="aprobado"
    if nota<=3:
        examen="No Aprobado"
    return examen
print(evaluacion(nota_alumn))
 