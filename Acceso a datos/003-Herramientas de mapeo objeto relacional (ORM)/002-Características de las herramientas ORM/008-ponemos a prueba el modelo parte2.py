import mysql.connector

class Profesor:
    def __init__(self):
      self.nombre = None
      self.descripcion = None
      self.alumnos =  None
clase = "Profesor"

conexion = mysql.connector.connect(
  host='localhost',  
  database='accesoadatos', 
  user='root',  
  password=''  
)
cursor = conexion.cursor(dictionary=True)

profesores = []

peticion = "SELECT * FROM " + clase
cursor.execute(peticion)

filas = cursor.fetchall()
for fila in filas:
  profesor = Profesor()
  for clave, valor in fila.items():
    setattr(profesor, clave, valor)
  profesores.append(profesor)
  # Ahora busco tablas externas
  for clave, valor in vars(profesor).items():
    if valor == None:
      setattr(profesor, clave, [])
      print("Tabla externa en: ", clave)
      peticion2 = "SELECT " + clave + " FROM " + clave + " WHERE FK = " + str(profesor.Identificador)
      cursor.execute(peticion2)
      filas2 = cursor.fetchall()
      for fila2 in filas2:
        print(fila2)
        getattr(profesor, clave).append(fila2[clave])
    

print(vars(profesores[0]))

profesores = []
conexion.commit()