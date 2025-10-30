🧩 Gestor de Usuarios con Flask
Este proyecto es una aplicación web sencilla desarrollada con Flask que permite registrar, almacenar y visualizar usuarios mediante un formulario HTML. Los datos se guardan en un archivo JSON local para persistencia.

🚀 Funcionalidades principales
Página de inicio (/): Muestra el título del gestor y dos botones para navegar al formulario de registro o a la lista de usuarios.

Formulario de registro (/formulario): Permite introducir los datos de un nuevo usuario (email, nombre, apellidos, contraseña, teléfono y edad).

Registro de usuario (/usuarios): Recibe los datos del formulario, crea una instancia de Persona (definida en clase_persona.py), la añade a la lista de usuarios y guarda todo en un archivo JSON.

Visualización de usuarios (/MostrarUsuarios): Lee el archivo JSON y muestra una lista con los datos básicos de cada usuario registrado.

🗃️ Estructura de datos
Los usuarios se almacenan como objetos de la clase Persona, que debe incluir un método to_dict() para convertirlos a formato JSON.


📦 Requisitos
Python 3.x

Flask

Archivo clase_persona.py con la clase Persona y su método to_dict()

🛠️ Ejecución
bash
python app.py
La aplicación se ejecuta en modo debug para facilitar el desarrollo.
