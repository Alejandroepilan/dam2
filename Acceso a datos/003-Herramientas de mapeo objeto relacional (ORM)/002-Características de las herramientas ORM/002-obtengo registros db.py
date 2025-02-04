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
cursor = conexion.cursor(dictionary=True)


peticion = "SELECT * FROM " + clase
cursor.execute(peticion)

filas = cursor.fetchall()
for fila in filas:
  print(fila)


personas = []
conexion.commit()