class Coche():

    def desplazamiento (self):

        print("Me desplazo usando 4 ruedas")

class Moto():
    def desplazamiento(self):
         print("Me desplazo en dos ruedas")

class camion():
      
      def desplazamiento (self):
         print("Me desplazo en 6 ruedas")

def desplazamientoVehiculo(vehiculo):   #Polimorfismo Se creo una funcion

    vehiculo.desplazamiento()

miVehiculo=Coche()
desplazamientoVehiculo(miVehiculo) #Aqui se almacena el polimorfismo
