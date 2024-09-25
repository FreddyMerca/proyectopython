from tkinter import *

root=Tk()
root.title("Ejemplo")

playa=IntVar()
montana=IntVar()
turismoRural=IntVar()

def opcionesViaje():

    opcionEscogida=""

    if(playa.get()==1):

        opcionEscogida+=" Playa "

    if(montana.get()==1):

        opcionEscogida+=" Montana "

    if(turismoRural.get()==1):

        opcionEscogida+=" Turismo Rural "

    textoFinal.config(text=opcionEscogida)


miImagen=PhotoImage(file="avion2.png")
Label(root, image=miImagen)

frame=Frame(root)
frame.pack()


Label(frame, text="Elige Destino" , width=50).pack()


Checkbutton(frame, text="playa ", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña ", variable=montana, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo Rural ", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()