import json
import os
import errno
import tkinter as tk
from tkinter import messagebox

class Cliente:
  def __init__(self,idcliente, nuevonombre, nuevosapellidos, listapersonal, listaprofesional):
    self.idcliente = idcliente
    self.nombre = nuevonombre
    self.apellidos = nuevosapellidos
    self.emails = {"personal":listapersonal,"profesional":listaprofesional}
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

carpeta = "C:\\Users\\Alejandro\\Desktop\\dam2\\Acceso a datos\\001-Manejo de ficheros\\007-Excepciones detección y tratamiento\\basededatos"
continuas = True
clientes = []

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

def obtenerNuevoId():
  try:
    archivos = [int(f[:5]) for f in os.listdir(carpeta) if f.endswith(".json")] # Extrae los 5 primeros caracteres de cada nombre de archivo .json
    en_memoria = [int(c.idcliente) for c in clientes if c.idcliente.isdigit()] # Añade las id de los clientes en la array
    todos = archivos + en_memoria # Combina las id de los archivos y los clientes en array
    siguiente = max(todos) + 1 if todos else 1 # Obteniene el id mas alto y suma 1, si no hay id empieza desde 1
    return f"{siguiente:05d}" # Devuelve el numero como texto con 5 cifras, rellenando con ceros si hace falta
  except:
    return "00001"

def guardaCliente():
  id_actual = idcliente.get() # Obtenemos el id del cliente actual
  ruta = os.path.join(carpeta, id_actual + ".json") # Obtenemos la ruta del nuevo archivo JSON 

  if not id_actual:
    messagebox.showerror("Error", "El campo ID no puede estar vacío.")
    return

  if os.path.exists(ruta):
    messagebox.showerror("Error", f"El cliente con ID {id_actual} ya existe.")
    return

  global clientes
  clientes.append(
    Cliente(idcliente.get(), nombre.get(), apellidos.get(), personal.get(), profesional.get())
    )
  messagebox.showinfo("Info", f"Cliente {id_actual} añadido correctamente.")

   # Limpiar campos
  nombre.set("")
  apellidos.set("")
  personal.set("")
  profesional.set("")

  # Generar nuevo ID automáticamente
  idcliente.set(obtenerNuevoId())
     
def guardaDB():
  for cliente in clientes:
    with open(carpeta+"/"+cliente.idcliente+".json",'w') as archivo: # usamos with para abrir el archivo, se cierra solo al terminar
      json.dump(cliente.to_dict(),archivo,indent=4)
  messagebox.showinfo("Info", "Todos los clientes han sido guardados correctamente.")

ventana = tk.Tk()
marco = tk.Frame(ventana,padx=20,pady=20)
marco.pack(padx=20,pady=20)

# Configuración de la ventana
ventana.title("Gestor de clientes")
ventana.configure(bg="#f2f2f2")
marco.configure(bg="#f2f2f2")

nombre = tk.StringVar()
apellidos = tk.StringVar()
idcliente = tk.StringVar()
personal = tk.StringVar()
profesional = tk.StringVar()

tk.Label(marco,text="Id de cliente").pack(padx=10,pady=10)
tk.Entry(marco,textvariable=idcliente).pack(padx=10,pady=10)
idcliente.set(obtenerNuevoId()) # Inserta en el campo ID el siguiente ID disponible
tk.Label(marco,text="Nombre").pack(padx=10,pady=10)
tk.Entry(marco,textvariable=nombre).pack(padx=10,pady=10)
tk.Label(marco,text="Apellidos").pack(padx=10,pady=10)
tk.Entry(marco,textvariable=apellidos).pack(padx=10,pady=10)
tk.Label(marco,text="Email personal").pack(padx=10,pady=10)
tk.Entry(marco,textvariable=personal).pack(padx=10,pady=10)
tk.Label(marco,text="Email profesional").pack(padx=10,pady=10)
tk.Entry(marco,textvariable=profesional).pack(padx=10,pady=10)
tk.Button(marco,text="Guardamos este cliente",command=guardaCliente).pack(padx=10,pady=10)
tk.Button(marco,text="Guardamos todos los clientes a base de datos",command=guardaDB).pack(padx=10,pady=10)

ventana.mainloop()