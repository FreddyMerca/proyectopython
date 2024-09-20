class Coche():
   
   def __init__(self): #Contructor--> es el que le va a dar los estados inicales a los objetos
      self.__largoChasis=250
      self.__anchoChasis=120
      self.__ruedas=4 #las dos __ Encapsulada, no puede ser modificada desde fuera de la clase
      self.__enmarcha=False


    #def function ya no es una funcion sino un metodo ya que esta identado dentro de la clase
   
   def arrancar(self,arrancamos):  #Self hace referencia a la instancia perteneciente a la clase y se le crea un parametros ·arrancamos
      
      self.__enmarcha=arrancamos #la propiedad en marcha va a ser igual a los que le pusimos en el metodo arrancamos
      if(self.__enmarcha):
         chequeo=self.__chequeo_int()

      if(self.__enmarcha and chequeo): #SI la variable self.enmarcha es Tru entonces
        return "El coche esta en marcha"
      elif(self.__enmarcha and chequeo==False):
         return "Algo esta mal, revisa antes de arrancar"
                   
      else:
         return "El coche no esta en marcha"

   def estado(self):
      print("El coche tiene ", self.__ruedas, "ruedas y Un ancho de ", self.__anchoChasis, "y un largo de ",self.__largoChasis)

   def __chequeo_int(self): #metodo encapsulado
      print("-Realizando Chequeo Interno-")
      self.gasolina="OK"
      self.aceita="OK"
      self.puertas="Cerradas"

      if(self.gasolina=="OK" and self.aceita=="OK" and self.puertas=="Cerradas"):
         return True
      else:
         return False


miCoche=Coche() #Crear Objeto o instanciar una clase en este caso class coche()
print(miCoche.arrancar(True)) #Llamamos al objeto miCoche y le ponemos el metodo arrancar en True

miCoche.estado() #llamada al estado del objeto con el metodo estado 

print("-------------------")

#Crear segundo objeto u instancia

miCoche2=Coche()
print(miCoche2.arrancar(False)) #Llamamos al objeto miCoche2 y le ponemos el metodo arrancar en False

miCoche2.estado() #llamada al estado del objeto
