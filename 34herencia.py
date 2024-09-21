class Vehiculos():

    def __init__(self, marca, modelo):

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


miMoto=Moto("Honda", "CBR")
miMoto.estado() #Aqui se imprime el ultimo metodo similar que se usa en este caso el de moto 
miMoto.caballito()
MiFurgoneta=Furgoneta("Renault", "FBR")
MiFurgoneta.arrancar()
MiFurgoneta.estado()
print(MiFurgoneta.carga(True)) 

