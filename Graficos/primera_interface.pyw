from tkinter import * #Importamos la libreria tkinter 

raiz=Tk() #se costruye la raiza con una vairable de cualquier nombre a la clase tk()
raiz.title("First Window")
raiz.resizable(1,1) #Para que no sea redimensinable la ventana ancho, alto. Es booleano 1-0 true-false
raiz.iconbitmap("D:\Phyton\Graficos\OIP.ico") #Cambiar el icono de la ventana, en los parentesis va la ruta
raiz.geometry("650x350") #Tamaña por defecto de la ventana

raiz.config(bg="green") #Color de la ventana

raiz.mainloop() #metodo mainloop, siempre debe estar al final

