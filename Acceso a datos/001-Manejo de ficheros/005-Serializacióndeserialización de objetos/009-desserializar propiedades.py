import random
import math

class Npc:
  def __init__(self):
    self.x = random.randint(0,512)
    self.y = random.randint(0,512)
    self.angulo = random.random()*math.pi*2

npcs = []

archivo = open("basededatos.txt",'r')
contenido = archivo.read()
print(contenido)

objetos = contenido.split("|")
for objeto in objetos:
  try:
    propiedades = objeto.split(",")
    print(propiedades)
    npcs.append(Npc(propiedades[0],propiedades[1],propiedades[2]))
  except:
    print("Ha ocurrido algún error")

for npc in npcs:
  print(npc.x,npc.y,npc.angulo)