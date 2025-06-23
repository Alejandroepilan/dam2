import random
import math

class Npc:
  def __init__(self, x=None, y=None, angulo=None, rol=None): # Este constructor acepta datos si vienen del archivo, pero tambien puede generar npc aleatorios si no se le pasan
    self.x = float(x) if x is not None else random.randint(0, 512)
    self.y = float(y) if y is not None else random.randint(0, 512)
    self.angulo = float(angulo) if angulo is not None else random.random() * math.pi * 2
    self.rol = rol.strip() if rol else random.choice(["comerciante", "enemigo", "neutral", "curandero"])

npcs = []

# Intentamos abrir el archivo de texto que contiene los datos serializados
# Si no existe, creamos una variable contenido vacia para que no falle el programa
try:
  archivo = open("basededatos.txt",'r')
  contenido = archivo.read()
  #print(contenido)
except:
  print("No se ha podido abrir el archivo")
  contenido = ""

objetos = contenido.split("|")

for objeto in objetos:
  try:
    propiedades = objeto.split(",") # Separamos las propiedades por comas
    if len(propiedades) == 4: # Comprobamos que hay 4 propiedades para que no falle el programa
      npcs.append(Npc(propiedades[0], propiedades[1], propiedades[2], propiedades[3]))
    else:
      print("Formato incorrecto:", propiedades)
  except:
    print("Ha ocurrido algún error")

for npc in npcs:
  print(npc.x, npc.y, npc.angulo, npc.rol)