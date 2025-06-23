import csv
import pandas as pd
import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="crimson"
)
cursor = conexion.cursor()
peticion = "INSERT INTO clientes (Identificador) VALUES (NULL)"     # Inserto un cliente vacio
print(peticion)
cursor.execute(peticion)
conexion.commit()

diccionario = {}
archivo = open('C:\\xampp\\htdocs\\dam2\\Sistemas de gestión empresarial\\proyecto\\023-utilidades\\utilidades\\importador\\mapeado.csv', mode='r')
lectorcsv = csv.DictReader(archivo)

mapeado = {}

for fila in lectorcsv:
  mapeado[fila['excel']] = fila['mysql']

#print(mapeado)

print("-------------------------------------------------------------------------------")

contenido = pd.read_excel('C:\\xampp\\htdocs\\dam2\\Sistemas de gestión empresarial\\proyecto\\023-utilidades\\utilidades\\importador\\clientes.xlsx')
diccionario = contenido.to_dict()
#print(diccionario)

for clave in diccionario:
  #print("Clave excel:",clave)
  #print("Valor clave:",diccionario[clave][0])
  #print("Columna MySQL:",mapeado[clave])
  #print("--------------------------------------------------")
  peticion = "UPDATE clientes SET "+str(mapeado[clave])+" = '"+str(diccionario[clave][0])+"';"
  print(peticion)