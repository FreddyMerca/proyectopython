import sqlite3 #importar libreria de sql

miConexion=sqlite3.connect("Primera base") #Se crea la conexion, aprovisionado una variiable al import sqlite3 con el metodo connect y el nombre de la BD


miConexion.close()

