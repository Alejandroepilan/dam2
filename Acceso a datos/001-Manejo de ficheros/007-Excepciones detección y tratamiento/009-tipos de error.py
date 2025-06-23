import json
import os
import errno

class Cliente:
  def __init__(self):
    self.idcliente = None
    self.nombre = None
    self.apellidos = None
    self.emails = {"personal":[],"profesional":[]}
  def to_dict(self):
    return {
      "nombre": self.nombre,
      "apellidos": self.apellidos,
      "emails": self.emails
    }

class Producto:
  def __init__(self):
    self.nombre = None
    self.precio = None
    self.peso = None
    self.dimensiones = {"x":None,"y":None,"z":None}

carpeta = "basededatos"
continuas = True
try:
  os.makedirs(carpeta)
except OSError as e:
  if e.errno == errno.EEXIST:
    print(f"La carpeta ya existe.")
  elif e.errno == errno.EACCES:
    continuas = False
    print("Error de permisos en la carpeta - no puedo guardar")
  else:
    print(f"Unexpected error: {e}")

clientes = []

clientes.append(Cliente())
clientes[-1].idcliente = "00001"
clientes[-1].nombre = "Alejandro"
clientes[-1].apellidos = "Epila Navarro"
clientes[-1].emails['profesional'].append("info@alejandroepila.com")
clientes[-1].emails['profesional'].append("info@aepila.com")
clientes[-1].emails['personal'].append("alejandroepilan@gmail.com")

clientes.append(Cliente())
clientes[-1].idcliente = "00002"
clientes[-1].nombre = "Jorge"
clientes[-1].apellidos = "lopez martinez"
clientes[-1].emails['profesional'].append("Jorge@alejandroepila.com")
clientes[-1].emails['profesional'].append("Jorge@aepila.com")
clientes[-1].emails['personal'].append("Jorge@gmail.com")

for cliente in clientes:
  archivo = open(carpeta+"/"+cliente.idcliente+".json",'w')
  json.dump(cliente.to_dict(), archivo, indent=4)
  archivo.close()