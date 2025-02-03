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

peticion = "DROP TABLE IF EXISTS Persona"
cursor.execute(peticion)

peticion = "CREATE TABLE IF NOT EXISTS Persona (Identificador INT NOT NULL AUTO_INCREMENT, "

atributos = [attr for attr in dir(personas[0]) if not callable(getattr(personas[0], attr)) and not attr.startswith("__")]

for atributo in atributos:
  if(not isinstance(getattr(personas[0], atributo), list)):
    peticion += atributo+" VARCHAR(255) NOT NULL ,"
  else:
    peticion2 = "DROP TABLE IF EXISTS "+atributo+""
    cursor.execute(peticion2)
    peticion2 = "CREATE TABLE IF NOT EXISTS "+atributo+" (Identificador INT NOT NULL AUTO_INCREMENT, FK INT(255), "+atributo+" VARCHAR(255), PRIMARY KEY (Identificador))"
    cursor.execute(peticion2)

peticion += "PRIMARY KEY (Identificador))"


cursor.execute(peticion)

for indice, persona in enumerate(personas):
  peticion = "INSERT INTO Persona VALUES(NULL,"

  for atributo in atributos:
    if(not isinstance(getattr(persona, atributo), list)):
      peticion += "'"+str(getattr(persona, atributo))+"',"
    else:
      for elemento in getattr(persona, atributo):
        peticion2 = "INSERT INTO "+atributo+" VALUES(NULL, "+str(indice + 1)+", '"+str(elemento)+"')"
        cursor.execute(peticion2) 
  peticion = peticion[:-1]
  peticion += ");"
  cursor.execute(peticion)

conexion.commit()