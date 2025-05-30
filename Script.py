import os

carpeta = "/home/joey-sullivan/Documentos/Documentos"

os.chdir(carpeta)

for i, nombre_archivo in enumerate(os.listdir()):
    _, extension = os.path.splitext(nombre_archivo)
    nuevo_nombre = f"archivo_{i+1}{extension}"
    os.rename(nombre_archivo, nuevo_nombre)

print("¡Renombrado completo!")
