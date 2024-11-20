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

for i in range(0,numero):
  print(npcs[i].x, npcs[i].y, npcs[i].angulo)

