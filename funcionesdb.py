import sqlite3

def insertar_alumno(alumno):
    conn = sqlite3.connect('midatabase.db')
    c = conn.cursor()
    c.execute("INSERT INTO Alumnos VALUES (?,?,?)", (alumno.id, alumno.nombre, alumno.apellido))
    conn.commit()
    conn.close()


def select_by_name(nombre):
    conn = sqlite3.connect('midatabase.db')
    c = conn.cursor()
    rows = c.execute("SELECT * FROM Alumnos WHERE nombre = ?", (nombre,))
    
    for row in rows:
        print(row)
   
    conn.close()
