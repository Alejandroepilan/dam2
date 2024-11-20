import random
import math
import json

class Npc:
  def __init__(self):
    self.x = random.randint(0,512)
    self.y = random.randint(0,512)
    self.angulo = random.random()*math.pi*2

npcs = []
numero = 50

for i in range(0,numero):
  npcs.append(Npc())

cadena = []

for i in range(0,numero):
  cadena.append({"x":npcs[i].x,"y":npcs[i].y,"angulo":npcs[i].angulo})

json_formatted_str = json.dumps(cadena, indent=2)
print(json_formatted_str)
mibasededatos = open("basededatos.json",'w')
mibasededatos.write(json_formatted_str)
mibasededatos.close()