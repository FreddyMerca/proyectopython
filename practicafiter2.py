class Empleado:

    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    
    def __str__(self):

        return "{} Que trabaja como {} y tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)
    
listaEmpleados=[

        Empleado("Juan", "Lider Funcional", 7500000),
        Empleado("Freddy", "Operario", 4500000),
        Empleado("Lorena", "Enfermera", 3500000),
        Empleado("Leonor", "Contadora", 2500000),

    ]

salarios_altos=filter(lambda empleado:empleado.salario>3000000, listaEmpleados)

for empleado_salario in salarios_altos:

    print(empleado_salario)

