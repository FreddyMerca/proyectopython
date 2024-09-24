import pickle #Libreriia para serializar

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
        

coche1=Vehiculos("Mazda", "3CX")
coche2=Vehiculos("Nissan", "Murano")
coche3=Vehiculos("Renault", "Clio")

coches=[coche1, coche2, coche3]

fichero=open("loscoches", "wb") #w-writeble b-binary
pickle.dump(coches, fichero)

fichero.close()

del (fichero)



