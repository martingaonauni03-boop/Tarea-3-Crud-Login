from flask import Blueprint, render_template, request, session, redirect, url_for
from werkzeug.security import check_password_hash
from models.usuario_model import buscar_usuario

usuario_bp = Blueprint("usuario", __name__)


@usuario_bp.route("/", methods=["GET", "POST"])
def inicio():
    mensaje = ""

    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        usuario_db = buscar_usuario(usuario)

        if usuario_db and check_password_hash(usuario_db["password"], password):
            session["usuario"] = usuario_db["usuario"]
            return redirect(url_for("productos.listar_productos"))
        mensaje = "Usuario o contraseña incorrectos"

    return render_template("login.html", mensaje=mensaje)


@usuario_bp.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("usuario.inicio"))