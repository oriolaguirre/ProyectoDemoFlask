from flask import Flask, request, jsonify
import json, clase_persona
from types import SimpleNamespace

app = Flask(__name__)
usuarios = []
ruta_archivo = "c:/Users/34666/Desktop/DOCUMENTOS/Oriol/Curso Python/ProyectoFlask/usuarios.json"
@app.route("/",methods=["GET"])
def home():
    return """
    <h1>Gestor de usuarios</h1>
    <a href="/formulario">
      <button style='padding:10px 20px; font-size:16px;'>Añadir usuarios</button>
    </a>
    <a href="/MostrarUsuarios">
      <button style='padding:10px 20px; font-size:16px;'>Mostrar usuarios</button>
    </a>
    """
@app.route("/formulario", methods=["GET"])
def mostrar_formulario():
    return formulario()

def formulario():
    return """
    <h2>Registrar nuevo usuario</h2>
    <form action="/usuarios" method="POST">
      <label>Email:</label><input type="text" name="email" required><br>
      <label>Nombre:</label><input type="text" name="nombre" required><br>
      <label>Apellidos:</label><input type="text" name="apellidos" required><br>
      <label>Contraseña:</label><input type="password" name="contraseña" required><br>
      <label>Teléfono:</label><input type="text" name="telefono" required><br>
      <label>Edad:</label><input type="number" name="edad" required><br>
      <input type="submit" value="Registrar">
    </form>
    """
@app.route("/usuarios", methods=["POST"])
def agregar_usuario():
    nuevo_usuario = clase_persona.Persona(
        email=request.form["email"],
        nombre=request.form["nombre"],
        apellidos=request.form["apellidos"],
        contraseña=request.form["contraseña"],
        telefono=request.form["telefono"],
        edad=int(request.form["edad"])
    )
    usuarios.append(nuevo_usuario)

    # Guardar en archivo JSON
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        json.dump([u.to_dict() for u in usuarios], f, indent=4)

    # Definir el HTML completo
    html = """
    <h2>Usuario creado correctamente</h2>
    <a href="/">
      <button style='padding:10px 20px; font-size:16px; margin-top:20px;'>Volver al inicio</button>
    </a>
    <a href="/MostrarUsuarios">
      <button style='padding:10px 20px; font-size:16px; margin-top:20px;'>Ver usuarios</button>
    </a>
    """
    return html


@app.route("/MostrarUsuarios", methods=["GET", "POST"])
def mostrarUsuarios():
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        data = json.load(f)

    usuarios = [SimpleNamespace(**usuario) for usuario in data]

    html = "<h2>Usuarios registrados:</h2><ul>"
    for u in usuarios:
        html += f"<li> Email :{u.email} Nombre: {u.nombre} Apellidos :{u.apellidos} </li>"
    html += "</ul>"
    html += """
    <a href="/">
      <button style='padding:10px 20px; font-size:16px; margin-top:20px;'>Volver al inicio</button>
    </a>
    """
    return html
if __name__ == "__main__":
    app.run(debug=True)

