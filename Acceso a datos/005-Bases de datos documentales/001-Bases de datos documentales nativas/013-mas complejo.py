from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")     # Cambia la URL si tu MongoDB está en otra ubicación
basededatos = cliente["empresa"]                        # Reemplaza con el nombre de tu base de datos
coleccion = basededatos["clientes"]                     # Reemplaza con el nombre de tu colección

cliente = {"nombre": "Carlos", "apellidos": "González", 
           "correos": [
             {"tipo":"personal","correo":"email1@gmail.com"},
             {"tipo":"trabajo","correo":"email2@gmail.com"}]}

resultado = coleccion.insert_one(cliente)

if resultado:
  print(resultado)
else:
  print("Na")