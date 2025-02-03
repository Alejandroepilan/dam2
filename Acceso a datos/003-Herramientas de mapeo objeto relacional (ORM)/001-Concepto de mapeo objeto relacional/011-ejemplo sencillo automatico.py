import json

class Persona:
  def __init__(self,
    nuevonombre,
    nuevosapellidos,
    nuevaedad,
    nuevosemails):
    self.nombre = nuevonombre
    self.apellidos = nuevosapellidos
    self.edad = nuevaedad

personas = []

personas.append(Persona("Alejandro", "Epila", 20))
personas.append(Persona("Marcos", "Beltran", 26))