
import datetime
from src import *
from create_shortcut import create_shortcut_to_directory
import os
import shutil

timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H_%M_%S')
folder = '../backups/notionbackup_' + timestamp
dataBaseID = "731d20d7-7815-4dac-806e-bef4654f2467"
headers = {
  'Authorization': 'Bearer secret_lpa4riCCDmZuURvr2GgsQVtkAIXRlVk8M77OpYO5KJm',
  'Notion-Version': '2022-06-28',
  'Content-Type': 'application/json',
}

makeBackup(folder, headers,dataBaseID)
create_shortcut_to_directory(f'{os.getcwd()}/{folder}/result.json', 'data.lnk')

# Rutas del archivo de origen y carpeta de destino
archivo_origen = "data.lnk"
carpeta_destino = "../"
# Mover el archivo a la carpeta de destino y reemplazar si es necesario
try:
    shutil.move(archivo_origen, os.path.join(carpeta_destino, os.path.basename(archivo_origen)))
    print(f"El archivo '{archivo_origen}' ha sido movido a '{carpeta_destino}' y reemplazado si existía.")
except FileNotFoundError:
    print(f"El archivo '{archivo_origen}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error al mover el archivo: {str(e)}")
