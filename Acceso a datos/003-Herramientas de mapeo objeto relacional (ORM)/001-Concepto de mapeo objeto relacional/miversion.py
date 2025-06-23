import mysql.connector

class Producto:
  def __init__(self, nuevonombre, nuevadescripcion, nuevoprecio, nuevascategorias, nuevoscolores, nuevostock):
    self.nombre = nuevonombre
    self.descripcion = nuevadescripcion
    self.precio = nuevoprecio
    self.categorias = nuevascategorias
    self.colores = nuevoscolores
    self.stock = nuevostock

def obtenerAtributos(objeto): #Funcion que fevuelve los atributos de la clase
  return [attr for attr in dir(objeto) if not callable(getattr(objeto, attr)) and not attr.startswith("__")]

def crearTablaPrincipal(cursor, nombre_tabla, atributos, ejemplo_objeto):
  cursor.execute(f"DROP TABLE IF EXISTS {nombre_tabla}")
  peticion = f"CREATE TABLE IF NOT EXISTS {nombre_tabla} (Identificador INT NOT NULL AUTO_INCREMENT, "
  
  for campo in atributos: # Miramos el tipo de cada atributo para ponerlo en la tabla
    valor = getattr(ejemplo_objeto, campo)
    if isinstance(valor, list):
      continue
    elif isinstance(valor, float):
      tipo_mysql = "FLOAT"
    elif isinstance(valor, int):
      tipo_mysql = "INT"
    else:
      tipo_mysql = "VARCHAR(255)"
    peticion += f"{campo} {tipo_mysql} NOT NULL, "
  
  peticion += "PRIMARY KEY (Identificador))"
  cursor.execute(peticion)

def crearTablaSecundaria(cursor, campo):
  cursor.execute(f"DROP TABLE IF EXISTS {campo}")
  cursor.execute(
    f"""CREATE TABLE IF NOT EXISTS {campo} (
      Identificador INT NOT NULL AUTO_INCREMENT,
      FK INT,
      {campo} VARCHAR(255),
      PRIMARY KEY (Identificador)
    )"""
  )

def insertarProducto(cursor, producto, nombre_tabla, atributos, id_producto):
  valores = []
  for campo in atributos:
    valor = getattr(producto, campo)
    if not isinstance(valor, list):
      valores.append(valor)
    else:
      for elemento in valor:
        cursor.execute(
          f"INSERT INTO {campo} (FK, {campo}) VALUES (%s, %s)",
          (id_producto, str(elemento))
        )
  campos_insert = ','.join(['NULL'] + ['%s'] * len(valores))
  cursor.execute(
    f"INSERT INTO {nombre_tabla} VALUES ({campos_insert})",
    valores
  )


conexion = mysql.connector.connect(
  host='localhost',
  database='accesoadatos',
  user='root',
  password=''
)
cursor = conexion.cursor()

productos = [
  Producto("Camiseta", "Camiseta fenomenal", 34.56, ['ropa', 'caballero'], ['rojo', 'blanco'], 50),
  Producto("Pantalón", "Pantalón para vestir", 56.43, ['ropa', 'señora'], ['negro', 'azul'], 30)
]

nombre_tabla = "Producto"
atributos = obtenerAtributos(productos[0])

crearTablaPrincipal(cursor, nombre_tabla, atributos, productos[0])

for campo in atributos: # Para cada atributo crea la tabla secundaria si es tipo list
  if isinstance(getattr(productos[0], campo), list):
    crearTablaSecundaria(cursor, campo)

for indice, producto in enumerate(productos):
  insertarProducto(cursor, producto, nombre_tabla, atributos, indice + 1)

conexion.commit()
conexion.close()
