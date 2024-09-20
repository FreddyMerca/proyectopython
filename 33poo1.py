class Coche():
   
   def __init__(self): #Contructor--> es el que le va a dar los estados inicales a los objetos
      self.largoChasis=250
      self.anchoChasis=120
      self.__ruedas=4 #Encapsulada, no puede ser modificada desde fuera de la clase
      self.enmarcha=False


    #def function ya no es una funcion sino un metodo ya que esta identado dentro de la clase
   
   def arrancar(self,arrancamos):  #Self hace referencia a la instancia perteneciente a la clase y se le crea un parametros ·arrancamos
      #el Self es el mismo que el this dec++ o java
      self.enmarcha=arrancamos #la propiedad en marcha va a ser igual a los que le pusimos en el metodo arrancamos

      if(self.enmarcha): #SI la variable self.enmarcha es Tru entonces
        return "El coche esta en marcha"
      else:
         return "El coche no esta en marcha"

   def estado(self):
      print("El coche tiene ", self.__ruedas, "ruedas y Un ancho de ", self.anchoChasis, "y un largo de ",self.largoChasis)
      
miCoche=Coche() #Crear Objeto o instanciar una clase en este caso class coche()
print(miCoche.arrancar(True)) #Llamamos al objeto miCoche y le ponemos el metodo arrancar en True

miCoche.estado() #llamada al estado del objeto con el metodo estado 

print("-------------------")

#Crear segundo objeto u instancia

miCoche2=Coche()
print(miCoche2.arrancar(False)) #Llamamos al objeto miCoche2 y le ponemos el metodo arrancar en False

miCoche2.estado() #llamada al estado del objeto
