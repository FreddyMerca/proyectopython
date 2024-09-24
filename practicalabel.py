from tkinter import *

root=Tk()
root.title("EMCALI")
miFrame=Frame(root, width=500, height=500)

miFrame.pack()
miImagen=PhotoImage(file="D:\Phyton\simpson.gif")
miLabel=Label(miFrame, image=miImagen)
#miLabel=Label(miFrame, text="Emcali Somos tu Empresa", fg="red", font=("Arial", 18))
miLabel.place(x=100, y=200)

root.mainloop()

