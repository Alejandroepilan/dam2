import mysql.connector

class Profesor:
    def __init__(self,
      nuevonombre,
      nuevadescripcion,
      nuevosalumnos):
      self.nombre = nuevonombre
      self.descripcion = nuevadescripcion
      self.alumnos =  nuevosalumnos
clase = "Profesor"

conexion = mysql.connector.connect(
  host='localhost',  
  database='accesoadatos', 
  user='root',  
  password=''  
)
cursor = conexion.cursor()

profesores = []

profesores.append(Profesor("Jose Vicente", "Profe de informatica", ['Marcos', 'Jose', 'Maria', 'Ana']))

peticion = "DROP TABLE IF EXISTS "+clase
cursor.execute(peticion)

peticion = "CREATE TABLE IF NOT EXISTS "+clase+" (Identificador INT NOT NULL AUTO_INCREMENT, "

atributos = [attr for attr in dir(profesores[0]) if not callable(getattr(profesores[0], attr)) and not attr.startswith("__")]

for atributo in atributos:
  if(not isinstance(getattr(profesores[0], atributo), list)):
    peticion += atributo+" VARCHAR(255) NOT NULL ,"
  else:
    peticion2 = "DROP TABLE IF EXISTS "+atributo+""
    cursor.execute(peticion2)
    peticion2 = "CREATE TABLE IF NOT EXISTS "+atributo+" (Identificador INT NOT NULL AUTO_INCREMENT, FK INT(255), "+atributo+" VARCHAR(255), PRIMARY KEY (Identificador))"
    cursor.execute(peticion2)

peticion += "PRIMARY KEY (Identificador))"


cursor.execute(peticion)

for indice, profesor in enumerate(profesores):
  peticion = "INSERT INTO "+clase+" VALUES(NULL,"

  for atributo in atributos:
    if(not isinstance(getattr(profesor, atributo), list)):
      peticion += "'"+str(getattr(profesor, atributo))+"',"
    else:
      for elemento in getattr(profesor, atributo):
        peticion2 = "INSERT INTO "+atributo+" VALUES(NULL, "+str(indice + 1)+", '"+str(elemento)+"')"
        cursor.execute(peticion2) 
  peticion = peticion[:-1]
  peticion += ");"
  cursor.execute(peticion)

conexion.commit()