class Persona:
    def __init__(self, email, nombre, apellidos, contraseña, telefono, edad):
        self.email = email
        self.nombre = nombre
        self.apellidos = apellidos
        self.contraseña = contraseña
        self.telefono = telefono
        self.edad = edad

    #Convierto a diccionario porque si no el json.dump da error       
    def to_dict(self):
            return {
                "email": self.email,
                "nombre": self.nombre,
                "apellidos": self.apellidos,
                "contraseña": self.contraseña,
                "telefono": self.telefono,
                "edad": self.edad
            }