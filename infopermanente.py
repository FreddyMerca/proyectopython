import pickle

class Persona:

    def __init__(self, nombre, genero, edad): #Constructor con los parametros
        self.nombre=nombre
        self.genero=genero
        self.edad=edad

        print("Se ha creado persona nueva", self.nombre)

    def __str__(self): #metodo str convierte en cadena de texto la info de un objeto
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
    #devuelve los datos en un solo fomato
    
class ListaPersonas:

    personas=[]

    def __init__(self):

        listaDePersonas=open("ficheroExterno", "ab+") #Se abre Fichero
        listaDePersonas.seek(0) #pone el cursor en el comienzo

        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se Cargaron {} personas del fichero externo".format(len(self.personas))) 
        
        except:
            print("El fichero esta vacio ")

        finally:
            listaDePersonas.close()
            del(listaDePersonas)            


    def agregarPersonas(self, p):
        self.personas.append(p) #la persona de variable p sera agregada a la lista de personas
        self.guardarPersonasFicheroExterno()

    def mostrarPersonas(self):

        for p in self.personas:
            print(p)

    def guardarPersonasFicheroExterno(self):
        ListaPersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas, ListaPersonas)
        del(ListaPersonas)

    def mostrarInfoFicheroExterno(self):
        print("La informacion del fichero externo es: ")

        for p in self.personas:
            print(p)


miLista=ListaPersonas() #Se cre la instancia
persona=Persona("Valery", "Femenino", 12) #Se crea la persona pertinente 
miLista.agregarPersonas(persona) #se le pasa al metodo agregar persona en p 
miLista.mostrarInfoFicheroExterno()
            

