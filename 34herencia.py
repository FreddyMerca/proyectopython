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

class moto(Vehiculos): #La clase Moto hereda los atributos de la clase Vehiculos
    pass

miMoto=moto("Honda", "CBR")

miMoto.estado()
