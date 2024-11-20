import random
import math

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

print(cadena)
##mibasededatos = open("basededatos.txt",'w')
##mibasededatos.write(cadena)
##mibasededatos.close()

