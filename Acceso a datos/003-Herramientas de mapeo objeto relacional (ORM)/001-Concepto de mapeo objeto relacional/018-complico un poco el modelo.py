import mysql.connector

class Persona:
  def __init__(self,
    nuevonombre,
    nuevosapellidos,
    nuevaedad,
    nuevoemail,
    nuevadireccion,
    nuevostelefonos):
    self.nombre = nuevonombre
    self.apellidos = nuevosapellidos
    self.edad = nuevaedad
    self.email = nuevoemail
    self.direccion = nuevadireccion
    self.telefonos = nuevostelefonos

conexion = mysql.connector.connect(
  host='localhost',  
  database='accesoadatos', 
  user='root',  
  password=''  
)
cursor = conexion.cursor()

personas = []

personas.append(Persona("Alejandro", "Epila", 20, "email1@gmail.com", "Calle 1", [123456789, 987654321]))
personas.append(Persona("Marcos", "Beltran", 26, "email2@gmail.com", "Calle 2", [123456789, 987654321]))

peticion = "DROP TABLE Persona"
cursor.execute(peticion)

peticion = "CREATE TABLE IF NOT EXISTS Persona ("

atributos = [attr for attr in dir(personas[0]) if not callable(getattr(personas[0], attr)) and not attr.startswith("__")]

for atributo in atributos:
  peticion += atributo+" VARCHAR(255) NOT NULL ,"

peticion = peticion[:-1]
peticion += ")"


cursor.execute(peticion)

for persona in personas:
  peticion = "INSERT INTO Persona VALUES("

  for atributo in atributos:
    peticion += "'"+str(getattr(persona, atributo))+"',"
  peticion = peticion[:-1]
  peticion += ");"
  cursor.execute(peticion)

conexion.commit()