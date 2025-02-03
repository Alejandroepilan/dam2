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
    self.emails = nuevosemails
  def to_dict(self):
    return {
      'nombre': self.nombre,
      'apellidos': self.apellidos,
      'edad': self.edad,
      'emails': self.emails
    }

personas = []

correosalejandro = [
  {
    'tipo': 'personal',
    'valor': 'email1@gmail.com'
  },
  {
    'tipo': 'trabajo',
    'valor': ['email2@gmail.com', 'email3@gmail.com']
  }
]

personas.append(Persona("Alejandro", "Epila", 20, correosalejandro))

diccionario = [persona.__dict__ for persona in personas]

archivo = open("personas.json", "w", encoding="utf-8")
json.dump(diccionario, archivo, ensure_ascii=False, indent=4)
archivo.close()