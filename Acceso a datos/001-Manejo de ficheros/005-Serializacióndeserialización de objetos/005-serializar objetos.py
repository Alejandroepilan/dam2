import random

class Npc:
  def __init__(self):
    self.x = random.randint(0,512)
    self.y = random.randint(0,512)

npcs = []
numero = 50

for i in range(0,numero):
  npcs.append(Npc())

for i in range(0,numero):
  print(npcs[i])

