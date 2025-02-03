import mysql.connector

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
    'valor': 'email2@gmail.com'
  }
]

personas.append(Persona("Alejandro", "Epila", 20, ["email1@gmail.com", "email2@gmail.com"]))
personas.append(Persona("Juan", "Garcia", 50, ["email3@gmail.com", "email4@gmail.com"]))

conexion = mysql.connector.connect(
  host='localhost',  
  database='accesoadatos', 
  user='root',  
  password=''  
)
cursor = conexion.cursor()

for persona in personas:
  correos = ", ".join(persona.emails)
  peticion = f"""
  INSERT INTO personas 
  VALUES (NULL,
  '{persona.nombre}',
  '{persona.apellidos}',
  {persona.edad},
  '{correos}');
  """
  cursor.execute(peticion)
conexion.commit()