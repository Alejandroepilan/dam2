import mysql.connector

class Producto:
    def __init__(self):
      self.nombre = None
      self.descripcion = None
      self.precio = None
      self.categorias =  None
      self.colores = None
      self.stock = None
clase = "Producto"

conexion = mysql.connector.connect(
  host='localhost',  
  database='accesoadatos', 
  user='root',  
  password=''  
)
cursor = conexion.cursor(dictionary=True)

productos = []

peticion = "SELECT * FROM " + clase
cursor.execute(peticion)

filas = cursor.fetchall()
for fila in filas:
  producto = Producto()
  for clave, valor in fila.items():
    setattr(producto, clave, valor)
  productos.append(producto)
  # Ahora busco tablas externas
  for clave, valor in vars(producto).items():
    if valor == None:
      setattr(producto, clave, [])
      print("Tabla externa en: ", clave)
      peticion2 = "SELECT " + clave + " FROM " + clave + " WHERE FK = " + str(producto.Identificador)
      cursor.execute(peticion2)
      filas2 = cursor.fetchall()
      for fila2 in filas2:
        print(fila2)
        getattr(producto, clave).append(fila2[clave])
    

print(vars(productos[0]))

productos = []
conexion.commit()