# Sistema CRUD con Flask

## Descripción
Este proyecto consiste en una aplicación web desarrollada en Python con Flask. Se utilizó el patrón MVC 
para organizar el código y SQLite para guardar la información.

## Funciones
- Inicio y cierre de sesión.
- Registro de productos.
- Visualización de productos.
- Edición y eliminación de productos.
- Protección de páginas mediante sesiones.
- Contraseñas almacenadas con hash.

## Tecnologías utilizadas
- Python y Flask
- SQLite
- HTML y CSS

## Ejecución
Para ejecutar el proyecto se deben instalar las dependencias:

`pip install -r requirements.txt`

Después, ejecutar:

`python app.py`

Finalmente, ingresar desde el navegador a:

`http://127.0.0.1:5000/`

## Usuario de prueba
Usuario: admin  
Contraseña: 1234

## Estructura MVC
Modelo: maneja la información de la base de datos.
Vista: muestra las páginas HTML.
Controlador: maneja las rutas y las funciones del sistema.