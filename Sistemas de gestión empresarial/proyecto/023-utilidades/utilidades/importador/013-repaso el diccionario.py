import csv
import pandas as pd

diccionario = {}
archivo = open('C:\\xampp\\htdocs\\dam2\\Sistemas de gestión empresarial\\proyecto\\023-utilidades\\utilidades\\importador\\mapeado.csv', mode='r')
lectorcsv = csv.DictReader(archivo)

mapeado = {}

for fila in lectorcsv:
  mapeado[fila['excel']] = fila['mysql']

print(mapeado)

print("-------------------------------------------------------------------------------")

contenido = pd.read_excel('C:\\xampp\\htdocs\\dam2\\Sistemas de gestión empresarial\\proyecto\\023-utilidades\\utilidades\\importador\\clientes.xlsx')
diccionario = contenido.to_dict()
print(diccionario)

for clave in diccionario:
  print("Clave excel:",clave)
  print("Valor clave:",diccionario[clave][0])
  print("Columna MySQL:",mapeado[clave])
  print("--------------------------------------------------") 