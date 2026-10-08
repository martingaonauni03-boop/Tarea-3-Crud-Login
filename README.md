# Sistema de Gestión de Productos con Flask

## Descripción
Aplicación web desarrollada en Python utilizando Flask y el patrón de arquitectura MVC (Modelo-Vista-Controlador). Permite administrar productos mediante operaciones CRUD y cuenta con un sistema de inicio de sesión.

## Funcionalidades
- Inicio y cierre de sesión.
- Autenticación con contraseñas almacenadas mediante hash.
- Protección de rutas mediante sesiones.
- Registro de nuevos productos.
- Visualización de productos.
- Edición de productos existentes.
- Eliminación de productos con confirmación.
- Almacenamiento de información en SQLite.

## Tecnologías utilizadas
- Python
- Flask
- SQLite
- HTML
- CSS
- Jinja2
- Werkzeug

## Arquitectura MVC
- **Modelo:** archivos de la carpeta `models/`, encargados del acceso a la base de datos.
- **Vista:** archivos HTML de la carpeta `templates/`, encargados de presentar la interfaz.
- **Controlador:** archivos de la carpeta `controllers/`, encargados de procesar las solicitudes y conectar modelos y vistas.

## Instalación y ejecución

1. Clonar el repositorio.
2. Abrir la carpeta del proyecto en una terminal.
3. Crear un entorno virtual:

```bash
python -m venv venv
```

4. Activar el entorno virtual en Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

5. Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

6. Ejecutar la aplicación:

```bash
python app.py
```

7. Abrir en el navegador:

```text
http://127.0.0.1:5000/
```

La base de datos SQLite y el usuario administrador de demostración se crean automáticamente durante el primer inicio.

## Acceso de demostración
- **Usuario:** admin
- **Contraseña:** 1234

Estas credenciales se utilizan únicamente con fines académicos y de demostración.

## Estructura del proyecto

```text
flask_crud_login/
├── app.py
├── controllers/
├── models/
├── templates/
├── static/
├── requirements.txt
├── .gitignore
└── README.md
```

## Consideraciones
Este proyecto fue desarrollado con fines académicos. Para utilizarlo en producción sería necesario configurar una clave secreta segura, desactivar el modo de depuración y reforzar las medidas de seguridad.