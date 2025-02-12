import tkinter as tk
from tkinter import filedialog

ventana = tk.Tk()

marco = tk.Frame(ventana)
marco.pack(padx=10,pady=10)

anchura = tk.IntVar()

def seleccionaEntrada():
  ruta = filedialog.askopenfilename()
  print("La ruta de tu video es:",ruta)

selector_video_entrada = tk.Button(
  marco,
  text="Selecciona el video de entrada",
  command=seleccionaEntrada
  )

selector_video_entrada.pack(padx=50,pady=50);

tk.Label(
  marco,
  text="Indica la anchura de salida que quieres"
  ).pack(padx=50,pady=20);

tk.Entry(
  marco,
  textvariable=anchura).pack(padx=50,pady=20);

ventana.mainloop()