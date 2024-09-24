import pickle

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
   

ficheroApertura=open("loscoches", "rb")
misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
    print(c.estado()) #Se imprime el c del for con el metodo def estado

