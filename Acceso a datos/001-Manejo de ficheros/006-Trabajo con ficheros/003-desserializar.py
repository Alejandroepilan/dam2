import random
import math
import json

class Npc:
  def __init__(self,nuevax,nuevay,nuevoangulo):
    self.x = nuevax
    self.y = nuevay
    self.angulo = nuevoangulo

npcs = []

with open('basededatos.json', 'r') as archivo:
  datos = json.load(archivo)

for elemento in datos:
  npcs.append(Npc(elemento['x'],elemento['y'],elemento['angulo']))

for npc in npcs:
  print(npc.x,npc.y,npc.angulo)