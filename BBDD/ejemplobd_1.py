import sqlite3 #importar libreria de sql

miConexion=sqlite3.connect("PrimeraBase") #Se crea la conexion, aprovisionado una variiable al import sqlite3 con el metodo connect y el nombre de la BD
miCursor=miConexion.cursor() #Se cre el cursor
#miCursor.execute("CREATE TABLE productos(nombre_articulo VARCHAR(50), precio INT, seccion VARCHAR(20))")
miCursor.execute("INSERT INTO productos VALUES('Balon',15,'Deportes')")

#variosProductos=[

   # ("Camiseta",10,"Deportes"),
    #("Jarron",50,"Ceramina"),
    #("Camion",70,"Jugueteria")


#]

miCursor.execute("SELECT * FROM productos")
variosProductos=miCursor.fetchall()

print(variosProductos)

#miCursor.executemany("INSERT INT productos VALUES (?,?,?)", variosProductos)



miConexion.commit()

miConexion.close()

