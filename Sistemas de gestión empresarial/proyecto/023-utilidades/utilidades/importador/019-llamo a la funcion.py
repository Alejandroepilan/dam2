import csv
import pandas as pd
import mysql.connector
import tkinter as tk
from tkinter import filedialog

ruta_archivo_excel = None

def definir():
  print("archivo de entrada")
  global ruta_archivo_excel
  ruta_archivo_excel = tk.filedialog.askopenfilename()

def vamosAlla():
  global ruta_archivo_excel
  print("archivo de entrada")

  conexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="crimson"
  )
  cursor = conexion.cursor()

  contenidoglobal = pd.read_excel(ruta_archivo_excel)
  lineas = len(contenidoglobal)

  for i in range(0, lineas):
    peticion = "INSERT INTO "+nombre_tabla.get()+" (Identificador) VALUES (NULL)"     # Inserto un cliente vacio
    print(peticion)
    cursor.execute(peticion)
    conexion.commit()

    peticion = "SELECT Identificador FROM "+nombre_tabla.get()+" ORDER BY Identificador DESC LIMIT 1" # Ultimo id insertado
    cursor.execute(peticion)
    resultado = cursor.fetchall()
    identificador = resultado[0][0]

    diccionario = {}
    archivo = open('C:\\xampp\\htdocs\\dam2\\Sistemas de gestión empresarial\\proyecto\\023-utilidades\\utilidades\\importador\\mapeado.csv', mode='r')
    lectorcsv = csv.DictReader(archivo)

    mapeado = {}

    for fila in lectorcsv:
      mapeado[fila['excel']] = fila['mysql']

    #print(mapeado)

    print("-------------------------------------------------------------------------------")

    contenido = pd.read_excel('C:\\xampp\\htdocs\\dam2\\Sistemas de gestión empresarial\\proyecto\\023-utilidades\\utilidades\\importador\\clientes.xlsx')
    diccionario = contenido.to_dict()
    #print(diccionario)

    for clave in diccionario:
      #print("Clave excel:",clave)
      #print("Valor clave:",diccionario[clave][0])
      #print("Columna MySQL:",mapeado[clave])
      #print("--------------------------------------------------")
      peticion = "UPDATE "+nombre_tabla.get()+" SET "+str(mapeado[clave])+" = '"+str(diccionario[clave][i])+"' WHERE Identificador = "+str(identificador)+";"
      print(peticion)
      cursor.execute(peticion)
      conexion.commit()



ventana = tk.Tk()

nombre_tabla = tk.StringVar()

tk.Label(ventana,text="Primero carga el archivo de excel").pack(padx=10,pady=10)
tk.Button(ventana,text="Archivo de entrada",command=definir).pack(padx=10,pady=10)
tk.Label(ventana,text="Ahora indica el nombre de la tabla en la que vas a importar").pack(padx=10,pady=10)
tk.Entry(ventana,textvariable = nombre_tabla).pack(padx=10,pady=10)
tk.Label(ventana,text="Ahora ejecutamos").pack(padx=10,pady=10)
tk.Button(ventana,text="Vamos alla",command=vamosAlla).pack(padx=10,pady=10)

ventana.mainloop()