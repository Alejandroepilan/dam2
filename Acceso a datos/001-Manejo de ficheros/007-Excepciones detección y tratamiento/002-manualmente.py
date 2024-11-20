class Cliente:
  def __init__(self):
    self.nombre = None
    self.apellidos = None
    self.emails = {"personal":[],"profesional":[]}

class Producto:
  def __init__(self):
    self.nombre = None
    self.precio = None
    self.peso = None
    self.dimensiones = {"x":None,"y":None,"z":None}

clientes = []
clientes.append(Cliente())

clientes[-1].nombre = "Alejandro"
clientes[-1].apellidos = "Epila Navarro"
clientes[-1].emails['profesional'].append("info@alejandroepila.com")
clientes[-1].emails['profesional'].append("info@aepila.com")
clientes[-1].emails['personal'].append("alejandroepilan@gmail.com")

print(clientes[-1].emails)