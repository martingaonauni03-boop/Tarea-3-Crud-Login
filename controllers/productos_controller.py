from flask import Blueprint, render_template, request, session, redirect, url_for

from models.productos_model import (
    obtener_productos,
    agregar_producto,
    actualizar_producto,
    eliminar_producto_db,
    obtener_producto_por_id
)

productos_bp = Blueprint("productos", __name__)

@productos_bp.route("/productos")
def listar_productos():
    if "usuario" not in session:
        return redirect(url_for("usuario.inicio"))

    lista_productos = obtener_productos()

    return render_template("productos.html", productos=lista_productos)

@productos_bp.route("/productos/nuevo", methods=["GET", "POST"])
def nuevo_producto():
    if "usuario" not in session:
        return redirect(url_for("usuario.inicio"))

    if request.method == "POST":
        nombre = request.form["nombre"]
        categoria = request.form["categoria"]
        precio = request.form["precio"]
        stock = request.form["stock"]

        agregar_producto(nombre, categoria, precio, stock)

        return redirect(url_for("productos.listar_productos"))

    return render_template("nuevo_producto.html")

@productos_bp.route("/productos/editar/<int:id>", methods=["GET", "POST"])
def editar_producto(id):
    if "usuario" not in session:
        return redirect(url_for("usuario.inicio"))

    producto = obtener_producto_por_id(id)

    if producto is None:
        return "Producto no encontrado", 404

    if request.method == "POST":
        nombre = request.form["nombre"]
        categoria = request.form["categoria"]
        precio = request.form["precio"]
        stock = request.form["stock"]

        actualizar_producto(id, nombre, categoria, precio, stock)

        return redirect(url_for("productos.listar_productos"))

    return render_template("editar_producto.html", producto=producto)


@productos_bp.route("/productos/eliminar/<int:id>", methods=["POST"])
def eliminar_producto(id):
    if "usuario" not in session:
        return redirect(url_for("usuario.inicio"))

    eliminar_producto_db(id)

    return redirect(url_for("productos.listar_productos"))