class Persona():

    def __init__(self, nombre, edad, cedula):

        self.nombre=nombre
        self.edad=edad
        self.cedula=cedula


    def descripcion (self):
        
        print ("Nombre: ", self.nombre, "Edad: ", self.edad, "Cedula: ", self.cedula)


class Empleado(Persona):
    
    def __init__(self, salario, antiguedad, nomempleado, edad_emple, cedula_emple): # En el meotodo se asignan las variables que se usaran en la funcion super

        super().__init__(nomempleado, edad_emple, cedula_emple) #Funcion Super llama al metodo de la funciona padre en este caso Nombre, edad, Cedula

        self.salario=salario #variable de Clase
        self.antiguedad=antiguedad

    def descripcion(self):
        super().descripcion() #Llama a la funcion descrpcion de la clase padre. 
        print("Salario: ", self.salario, "Antiiguedad: ", self.antiguedad)
    
Freddy=Empleado(4000400, 2, "Freddy", 37, "Cali")  #Objeto de tipo segun la clase
Freddy.descripcion()

print(isinstance(Freddy, Empleado)) #isintancia indica si el objeto pertenence a esa clase
