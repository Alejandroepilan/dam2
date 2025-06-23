import csv

diccionario = {}
archivo = open('C:\\xampp\\htdocs\\dam2\\Sistemas de gestión empresarial\\proyecto\\023-utilidades\\utilidades\\importador\\mapeado.csv', mode='r')
lectorcsv = csv.DictReader(archivo)

mapeado = []

for fila in lectorcsv:
  mapeado.append(fila)

print(mapeado)