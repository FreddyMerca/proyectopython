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

def calculo_comision(empleado):

    if(empleado.salario<=4000000):
        empleado.salario=empleado.salario*1.03
        return empleado

listaEmpleaComi=map(calculo_comision, listaEmpleados) #Primero argumento va la funcion y segundo argumento es la lista

for empleado in listaEmpleaComi:
    print(empleado)



#Funcion map sustituye el primer arguumento