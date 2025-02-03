import json

class Persona:
  def __init__(self,
    nuevonombre,
    nuevosapellidos,
    nuevaedad):
    self.nombre = nuevonombre
    self.apellidos = nuevosapellidos
    self.edad = nuevaedad

personas = []

personas.append(Persona("Alejandro", "Epila", 20))
personas.append(Persona("Marcos", "Beltran", 26))

atributos = [attr for attr in dir(personas[0]) if not callable(getattr(personas[0], attr)) and not attr.startswith("__")]

print(atributos)