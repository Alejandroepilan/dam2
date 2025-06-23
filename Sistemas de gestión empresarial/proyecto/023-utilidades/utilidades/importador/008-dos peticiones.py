import pandas as pd

contenido = pd.read_excel('C:\\xampp\\htdocs\\dam2\\Sistemas de gestión empresarial\\proyecto\\023-utilidades\\utilidades\\importador\\clientes.xlsx')
diccionario = contenido.to_dict()

print(diccionario)
print(diccionario['Direccion del cliente'][0])

for i in range(0,2):

  peticion = "INSERT INTO clientes VALUES (NULL, "

  for clave in diccionario:
    print(clave,diccionario[clave][i])
    peticion += clave + " = '" + str(diccionario[clave][i]) + "',"

  peticion = peticion[:-1] # Eliminar la última coma  

  peticion += ")"
  print(peticion)