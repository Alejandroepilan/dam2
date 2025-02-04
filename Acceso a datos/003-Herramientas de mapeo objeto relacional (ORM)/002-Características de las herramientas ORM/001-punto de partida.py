import mysql.connector

class Producto:
    def __init__(self,
      nuevonombre,
      nuevadescripcion,
      nuevoprecio,
      nuevascategorias):
      self.nombre = nuevonombre
      self.descripcion = nuevadescripcion
      self.precio = nuevoprecio
      self.categorias =  nuevascategorias
clase = "Producto"

conexion = mysql.connector.connect(
  host='localhost',  
  database='accesoadatos', 
  user='root',  
  password=''  
)
cursor = conexion.cursor()

personas = []

personas.append(Producto("Camiseta","Camiseta fenomenal",34.56,['ropa','caballero']))
personas.append(Producto("Pantalon","Pantalon para vestir",56.43,['ropa','señora']))

peticion = "DROP TABLE IF EXISTS "+clase
cursor.execute(peticion)

peticion = "CREATE TABLE IF NOT EXISTS "+clase+" (Identificador INT NOT NULL AUTO_INCREMENT, "

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
  peticion = "INSERT INTO "+clase+" VALUES(NULL,"

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