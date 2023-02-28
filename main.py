'''
En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna 
id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
'''
import sqlite3
from alumno import Alumno
import funcionesdb as db



conn = sqlite3.connect('midatabase.db')

c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS Alumnos (
            id INTEGER NOT NULL PRIMARY KEY,
            nombre TEXT,
            apellido TEXT)""")


al9 = Alumno(9, 'Facundo', 'Bordes')
al10 = Alumno(10, 'Cosme', 'Fulanito')
al11 = Alumno(11, 'Ariel', 'Ortega')

varios_alumnos = [
    (al9.id, al9.nombre, al9.apellido),
    (al10.id, al10.nombre, al10.apellido)
]

c.execute("INSERT INTO Alumnos VALUES(1, 'Juan', 'Perez')")
c.execute("INSERT INTO Alumnos VALUES(2, 'Daniel', 'Garcia')")
c.execute("INSERT INTO Alumnos VALUES(3, 'Juan', 'Denardi')")
c.execute("INSERT INTO Alumnos VALUES(4, 'Miguel', 'Ramirez')")
c.execute("INSERT INTO Alumnos VALUES(5, 'Fernando', 'Gomez')")
c.execute("INSERT INTO Alumnos VALUES(6, 'Marcelo', 'Hernandez')")
c.execute("INSERT INTO Alumnos VALUES(7, 'Daniel', 'Giri')")
c.execute("INSERT INTO Alumnos VALUES(8, 'Hugo', 'Maldonado')")

c.executemany("INSERT INTO Alumnos VALUES(?, ?, ?)", varios_alumnos)
conn.commit()

rows= c.execute("SELECT * FROM Alumnos WHERE nombre = 'Facundo'")

for row in rows:
    print(row)

db.insertar_alumno(al11)
db.select_by_name('Ariel')


