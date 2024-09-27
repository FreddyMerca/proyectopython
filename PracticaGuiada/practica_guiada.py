import os
import tkinter as tk
from tkinter import messagebox, scrolledtext
import sqlite3

# Definir la ruta de la base de datos en tu carpeta específica
db_ruta = r"D:\Python\PracticaGuiada\usuarios.db"

# Funciones para la base de datos
def conectar_bbdd():
    try:
        # Crear la carpeta si no existe
        os.makedirs(os.path.dirname(db_ruta), exist_ok=True)

        # Conectar a la base de datos en la ruta especificada
        conexion = sqlite3.connect(db_ruta)
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(50) NOT NULL,
                password VARCHAR(50) NOT NULL,
                apellido VARCHAR(50),
                direccion VARCHAR(100),
                comentarios TEXT
            )
        ''')
        conexion.commit()
        conexion.close()
        messagebox.showinfo("BBDD", "Base de datos creada correctamente en la ruta:\n" + db_ruta)
    except Exception as e:
        messagebox.showerror("Error", f"Error al conectar con la base de datos:\n{str(e)}")

def salir_app():
    respuesta = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    if respuesta == "yes":
        root.quit()

def limpiar_campos():
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_direccion.delete(0, tk.END)
    text_comentarios.delete("1.0", tk.END)

# CRUD Functions
def crear():
    conexion = sqlite3.connect(db_ruta)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios VALUES (NULL, ?, ?, ?, ?, ?)", 
                   (entry_nombre.get(), entry_password.get(), entry_apellido.get(), entry_direccion.get(), text_comentarios.get("1.0", tk.END)))
    conexion.commit()
    conexion.close()
    messagebox.showinfo("Crear", "Registro insertado correctamente")

def leer():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id=?", (entry_id.get(),))
    usuario = cursor.fetchone()
    conexion.close()
    
    if usuario:
        entry_nombre.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        entry_apellido.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)
        text_comentarios.delete("1.0", tk.END)
        
        entry_nombre.insert(0, usuario[1])
        entry_password.insert(0, usuario[2])
        entry_apellido.insert(0, usuario[3])
        entry_direccion.insert(0, usuario[4])
        text_comentarios.insert(tk.END, usuario[5])
    else:
        messagebox.showinfo("Leer", "No se encontró el registro")

def actualizar():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE usuarios SET 
        nombre=?, password=?, apellido=?, direccion=?, comentarios=? WHERE id=?
    """, (entry_nombre.get(), entry_password.get(), entry_apellido.get(), entry_direccion.get(), text_comentarios.get("1.0", tk.END), entry_id.get()))
    conexion.commit()
    conexion.close()
    messagebox.showinfo("Actualizar", "Registro actualizado correctamente")

def borrar_registro():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id=?", (entry_id.get(),))
    conexion.commit()
    conexion.close()
    messagebox.showinfo("Borrar", "Registro eliminado correctamente")

# Interfaz gráfica con tkinter
root = tk.Tk()
root.title("Gestión de Usuarios")
root.geometry("400x500")

# Menú
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Menú BBDD
bbdd_menu = tk.Menu(menu_bar, tearoff=0)
bbdd_menu.add_command(label="Conectar", command=conectar_bbdd)
bbdd_menu.add_separator()
bbdd_menu.add_command(label="Salir", command=salir_app)
menu_bar.add_cascade(label="BBDD", menu=bbdd_menu)

# Menú Borrar
borrar_menu = tk.Menu(menu_bar, tearoff=0)
borrar_menu.add_command(label="Borrar Campos", command=limpiar_campos)
menu_bar.add_cascade(label="Borrar", menu=borrar_menu)

# Menú CRUD
crud_menu = tk.Menu(menu_bar, tearoff=0)
crud_menu.add_command(label="Crear", command=crear)
crud_menu.add_command(label="Leer", command=leer)
crud_menu.add_command(label="Actualizar", command=actualizar)
crud_menu.add_command(label="Borrar", command=borrar_registro)
menu_bar.add_cascade(label="CRUD", menu=crud_menu)

# Menú Ayuda
ayuda_menu = tk.Menu(menu_bar, tearoff=0)
ayuda_menu.add_command(label="Licencia", command=lambda: messagebox.showinfo("Licencia", "Licencia MIT"))
ayuda_menu.add_command(label="Acerca de...", command=lambda: messagebox.showinfo("Acerca de", "Aplicación de gestión de usuarios v1.0"))
menu_bar.add_cascade(label="Ayuda", menu=ayuda_menu)

# Campos de entrada
frame_campos = tk.Frame(root)
frame_campos.pack(pady=20)

tk.Label(frame_campos, text="ID:").grid(row=0, column=0, padx=10, pady=5)
entry_id = tk.Entry(frame_campos)
entry_id.grid(row=0, column=1)

tk.Label(frame_campos, text="Nombre:").grid(row=1, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(frame_campos, fg="red")
entry_nombre.grid(row=1, column=1)

tk.Label(frame_campos, text="Password:").grid(row=2, column=0, padx=10, pady=5)
entry_password = tk.Entry(frame_campos, show="*")
entry_password.grid(row=2, column=1)

tk.Label(frame_campos, text="Apellido:").grid(row=3, column=0, padx=10, pady=5)
entry_apellido = tk.Entry(frame_campos)
entry_apellido.grid(row=3, column=1)

tk.Label(frame_campos, text="Dirección:").grid(row=4, column=0, padx=10, pady=5)
entry_direccion = tk.Entry(frame_campos)
entry_direccion.grid(row=4, column=1)

tk.Label(frame_campos, text="Comentarios:").grid(row=5, column=0, padx=10, pady=5)
text_comentarios = scrolledtext.ScrolledText(frame_campos, width=30, height=5)
text_comentarios.grid(row=5, column=1)

# Botones CRUD
frame_botones = tk.Frame(root)
frame_botones.pack(pady=20)

tk.Button(frame_botones, text="Crear", command=crear).grid(row=0, column=0, padx=10)
tk.Button(frame_botones, text="Leer", command=leer).grid(row=0, column=1, padx=10)
tk.Button(frame_botones, text="Actualizar", command=actualizar).grid(row=0, column=2, padx=10)
tk.Button(frame_botones, text="Borrar", command=borrar_registro).grid(row=0, column=3, padx=10)

root.mainloop()
