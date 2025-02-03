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

archivo = open("C:/xampp/htdocs/dam2/Acceso a datos/003-Herramientas de mapeo objeto relacional (ORM)/001-Concepto de mapeo objeto relacional/binario.bin", "rb")
personas = pickle.load(archivo)
archivo.close()

print(personas)