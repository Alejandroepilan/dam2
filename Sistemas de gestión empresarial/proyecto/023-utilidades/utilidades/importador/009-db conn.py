import pandas as pd
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="crimson"
)
cursor = conexion.cursor()

contenido = pd.read_excel('C:\\xampp\\htdocs\\dam2\\Sistemas de gestión empresarial\\proyecto\\023-utilidades\\utilidades\\importador\\clientes.xlsx')
diccionario = contenido.to_dict()

print(diccionario)
print(diccionario['Direccion del cliente'][0])

for i in range(0,2):

  peticion = "INSERT INTO clientes VALUES (NULL, "

  for clave in diccionario:
    print(clave,diccionario[clave][i])
    peticion += "'" + str(diccionario[clave][i]) + "',"

  peticion = peticion[:-1] # Eliminar la última coma  

  peticion += ")"
  print(peticion)

  cursor.execute(peticion)
  conexion.commit()