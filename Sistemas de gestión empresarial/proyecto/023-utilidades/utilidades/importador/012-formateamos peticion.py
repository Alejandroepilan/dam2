import csv
import pandas as pd

diccionario = {}
archivo = open('C:\\xampp\\htdocs\\dam2\\Sistemas de gestión empresarial\\proyecto\\023-utilidades\\utilidades\\importador\\mapeado.csv', mode='r')
lectorcsv = csv.DictReader(archivo)

mapeado = []

for fila in lectorcsv:
  mapeado.append(fila)

print(mapeado)

print("-------------------------------------------------------------------------------")

contenido = pd.read_excel('C:\\xampp\\htdocs\\dam2\\Sistemas de gestión empresarial\\proyecto\\023-utilidades\\utilidades\\importador\\clientes.xlsx')
diccionario = contenido.to_dict()
print(diccionario)