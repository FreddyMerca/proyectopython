from tkinter import *

root=Tk()

barraMenu=Menu(root) #Funcion Menu

root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir")

archivoEdicion=Menu(barraMenu, tearoff=0)

archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu)

archivoAyuda=Menu(barraMenu, tearoff=0)

archivoAyuda.add_command(label="Acerca de ")
archivoAyuda.add_command(label="Licencia ")

barraMenu.add_cascade(label="Archivo ", menu=archivoMenu)  #Agregar casacada del menu
barraMenu.add_cascade(label="Edicion ", menu=archivoEdicion)  #Agregar casacada del menu
barraMenu.add_cascade(label="Herramientas ", menu=archivoHerramientas)  #Agregar casacada del menu
barraMenu.add_cascade(label="Ayuda ", menu=archivoAyuda)  #Agregar casacada del menu


root.mainloop()