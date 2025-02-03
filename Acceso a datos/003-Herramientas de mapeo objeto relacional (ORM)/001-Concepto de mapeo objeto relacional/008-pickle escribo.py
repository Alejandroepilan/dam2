import pickle

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

archivo = open("C:/xampp/htdocs/dam2/Acceso a datos/003-Herramientas de mapeo objeto relacional (ORM)/001-Concepto de mapeo objeto relacional/binario.bin", "wb")
pickle.dump(personas, archivo)
archivo.close()