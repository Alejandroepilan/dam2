import json

class Npc:
  def __init__(self, nuevax, nuevay, nuevoangulo, nuevorol):
    self.x = nuevax
    self.y = nuevay
    self.angulo = nuevoangulo
    self.rol = nuevorol

npcs = []

try:
  with open('C:\\Users\\Alejandro\\Desktop\\dam2\\Acceso a datos\\001-Manejo de ficheros\\006-Trabajo con ficheros\\basededatos.json', 'r') as archivo:
    datos = json.load(archivo)
except FileNotFoundError:
  print("No se ha encontrado el archivo.")
  datos = []

for elemento in datos:
  npcs.append(Npc(elemento['x'],elemento['y'],elemento['angulo'], elemento['rol']))

for npc in npcs:
  print(npc.x, npc.y, npc.angulo, npc.rol)