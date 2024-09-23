class Vehiculos():

    def __init__(self, marca, modelo): #def __init se le conoce com constructor def es el metodo

        self.marca=marca #es igual a la marca que se le pase por parametro
        self.modelo=modelo #es igual al modelo que se le pase por parametro
        self.enmarcha=False
        self.acelera=False
        self.frena=False


    def arrancar(self):

        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo :" , self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando :", 
          self.acelera, "\nFrenando: ", self.frena)

class Moto(Vehiculos): #La clase Moto hereda los atributos de la clase Vehiculos
        hcaballito=""
        def caballito(self):
             #la clase moto le creamos un comportamiento que Vehiculos, tiene 5 heredados y el propio
             self.hcaballito="Haciendo Caballito"

        def estado(self):
            print("Marca: ", self.marca, "\nModelo :" , self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando :",   
            self.acelera, "\nFrenando: ", self.frena, "\nPirueta: ", self.hcaballito)
        
        #Se crea un metodo estado tambien en la clase moto debido a que no lo hereda desde vehiculo con la misma cantidad de parametros 

class Furgoneta(Vehiculos):
     
     def carga(self, cargam):
          self.cargado=cargam
          if(self.cargado):
               return "la furgoneta esta cargada"
          else:
               return "La furgoneta no est cargada"

class VElectricos(Vehiculos):
     def __init__(self):
          self.autonomia=100

     def cargarEnergia(self):
          self.cargando=True    

          
class BiciElectrica(VElectricos, Vehiculos): #Herencia multiple, herencia de dos o mas clases
     pass

