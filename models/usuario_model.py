import sqlite3

def conectar_db():
    conexion = sqlite3.connect("database.db")
    conexion.row_factory = sqlite3.Row
    return conexion


def buscar_usuario(nombre_usuario):
    conexion = conectar_db()

    usuario = conexion.execute(
        "SELECT * FROM usuarios WHERE usuario = ?",
        (nombre_usuario,)
    ).fetchone()

    conexion.close()

    return usuario