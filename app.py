from flask import Flask
import sqlite3
from werkzeug.security import generate_password_hash

from controllers.usuario_controller import usuario_bp
from controllers.productos_controller import productos_bp

app = Flask(__name__)
app.secret_key = "clave_secreta_desarrollo"
app.register_blueprint(usuario_bp)
app.register_blueprint(productos_bp)


def conectar_db():
    conexion = sqlite3.connect("database.db")
    conexion.row_factory = sqlite3.Row
    return conexion

def crear_tabla():
    conexion = conectar_db()

    # Crear tabla de productos
    conexion.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT NOT NULL,
        precio REAL NOT NULL,
        stock INTEGER NOT NULL
    )
    """)

    conexion.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)

    conexion.commit()
    conexion.close()

def crear_usuario_admin():
    conexion = conectar_db()

    usuario = conexion.execute(
        "SELECT * FROM usuarios WHERE usuario = ?",
        ("admin",)
    ).fetchone()

    if usuario is None:
        password_hash = generate_password_hash("1234")

        conexion.execute(
            "INSERT INTO usuarios (usuario, password) VALUES (?, ?)",
            ("admin", password_hash)
        )

        conexion.commit()

    conexion.close()


crear_tabla()
crear_usuario_admin()

if __name__ == "__main__":
    app.run(debug=True)