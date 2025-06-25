import os
from PIL import Image, ImageOps
from tqdm import tqdm

carpeta = "C:\\Users\\Alejandro\\Desktop\\dam2\\Acceso a datos\\001-Manejo de ficheros\\001-Clases asociadas a las operaciones de gestión de ficheros\\fotos"
formatos_validos = (".jpg", ".jpeg", ".png")

archivos = os.listdir(carpeta)

for archivo in tqdm(archivos, desc="Procesando imágenes", unit="img"):
    try:
        if archivo.lower().endswith(formatos_validos):
            ruta = os.path.join(carpeta, archivo)
            imagen = Image.open(ruta)
            imagen_gris = ImageOps.grayscale(imagen)
            imagen.close()
            imagen_gris.save(ruta)
            imagen_gris.close()
        else:
            print(f"Ignorado: {archivo}")
    except Exception as e:
        print(f"Error con {archivo}: {e}")
