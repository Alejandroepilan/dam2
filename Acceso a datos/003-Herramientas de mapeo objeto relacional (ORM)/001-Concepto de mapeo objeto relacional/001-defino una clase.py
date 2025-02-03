class Persona:
  def __init__(self,
    nuevonombre,
    nuevosapellidos,
    nuevaedad):
    self.nombre = nuevonombre
    self.apellidos = nuevosapellidos
    self.edad = nuevaedad

persona1 = Persona("Alejandro", "Epila", 20)
persona2 = Persona("Juan", "Garcia", 50)

print(persona1)