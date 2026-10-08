import sqlite3
def conectar_db():
    conexion = sqlite3.connect("database.db")
    conexion.row_factory = sqlite3.Row
    return conexion

def obtener_productos():
    conexion = conectar_db()

    productos = conexion.execute(
        "SELECT * FROM productos"
    ).fetchall()

    conexion.close()

    return productos

def agregar_producto(nombre, categoria, precio, stock):
    conexion = conectar_db()

    conexion.execute(
        """
        INSERT INTO productos (nombre, categoria, precio, stock)
        VALUES (?, ?, ?, ?)
        """,
        (nombre, categoria, precio, stock)
    )

    conexion.commit()
    conexion.close()



def actualizar_producto(id, nombre, categoria, precio, stock):
    conexion = conectar_db()

    conexion.execute(
        """
        UPDATE productos
        SET nombre = ?, categoria = ?, precio = ?, stock = ?
        WHERE id = ?
        """,
        (nombre, categoria, precio, stock, id)
    )

    conexion.commit()
    conexion.close()


def eliminar_producto_db(id):
    conexion = conectar_db()

    conexion.execute(
        "DELETE FROM productos WHERE id = ?",
        (id,)
    )

    conexion.commit()
    conexion.close()


def obtener_producto_por_id(id):
    conexion = conectar_db()

    producto = conexion.execute(
        "SELECT * FROM productos WHERE id = ?",
        (id,)
    ).fetchone()

    conexion.close()

    return producto
    




   