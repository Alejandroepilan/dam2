import pandas as pd

contenido = pd.read_excel('C:\\xampp\\htdocs\\dam2\\Sistemas de gestión empresarial\\proyecto\\023-utilidades\\utilidades\\importador\\clientes.xlsx')
diccionario = contenido.to_dict()

print(diccionario)
print(diccionario['Direccion del cliente'][0])

for clave in diccionario:
  print(clave,diccionario[clave][0])
