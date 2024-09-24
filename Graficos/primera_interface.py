from tkinter import * #Importamos la libreria tkinter 

raiz=Tk() #se costruye la raiza con una vairable de cualquier nombre a la clase tk()
raiz.title("EMCALI EICE ESP")
raiz.resizable(1,1) #Para que no sea redimensinable la ventana ancho, alto. Es booleano 1-0 true-false
raiz.iconbitmap("D:\Phyton\Graficos\emcali.ico") #Cambiar el icono de la ventana, en los parentesis va la ruta
#raiz.geometry("650x350") #Tamaña por defecto de la ventana
raiz.config(bg="yellow") #Color de la ventana
miFrame=Frame() #contruir el frame
miFrame.pack() #emapquetar el frame y lo posiciones
miFrame.config(bg="red")
miFrame.config(width="450", height="150") #tamaño del frame , tamaño fijo 
miFrame.config(relief="groove") #forma del borde
miFrame.config(bd="25")
miFrame.config(cursor="watch")
raiz.mainloop() #metodo mainloop, siempre debe estar al final

#guardar con extension .pyw para que al ejecutarlo no abra con la consola
