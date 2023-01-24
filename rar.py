#Script que extrae los datos de un archivo rar

# Importamos la libreria unrar
from unrar import rarfile
from unrar.rarfile import BadRarFile
import os, sys, pathlib, time, random

# Barra de progreso, por que no?
def progressBar(count_value, total, suffix=''):
    bar_length = 100
    filled_up_Length = int(round(bar_length* count_value / float(total)))
    percentage = round(100.0 * count_value/float(total),1)
    bar = '=' * filled_up_Length + '-' * (bar_length - filled_up_Length)
    sys.stdout.write('[%s] %s%s ...%s\r' %(bar, percentage, '%', suffix))
    sys.stdout.flush()

# Buscamos cualquier archivo con la extension .rar
for archivo in pathlib.Path(os.curdir).glob('*.rar'):
    archivo = str(archivo)

    try:
        print("Extrayendo archivo: ", archivo)
        rarfile.RarFile.extractall(rarfile.RarFile(archivo), os.curdir)
        for i in range(11):
            time.sleep(.01)
            progressBar(i, 10)
        print("\n Extraccion completada en la carpeta actual")

    except BadRarFile as badrar:
        print("No hay ningun archivo para descomprimir aqui", badrar)
