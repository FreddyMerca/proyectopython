from tkinter import *
raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red") #color dentro del cuadro de texto

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)

cuadroIde=Entry(miFrame)
cuadroIde.grid(row=2, column=1, padx=10, pady=10)


nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

ideLabel=Label(miFrame, text="Identificacion: ")
ideLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

raiz.mainloop()