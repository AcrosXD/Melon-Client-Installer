# https://cloud.mathildeuh.fr/index.php/s/8dbNeEP9adAfrgM/download/melon.rar

import wget
import time
from pathlib import Path
import os.path
from os import path
# import patoolib
import shutil
import subprocess
import zipfile


minecraftDir = input("Chemin d'accès vers vôte .minecraft:\n")
folder = str(Path(__file__).resolve().parent)
url = "https://cloud.mathildeuh.fr/index.php/s/n5MC5J4seNo33ZT/download/melon.zip"

if path.exists(folder + "/Client.zip"):
    print("Client.zip déjà téléchargé, installations en cours.")    
    time.sleep(1)

else:
    wget.download(url, folder + "/Client.zip" ) 
    time.sleep(1)

if path.exists(folder + "/Client"):
    print("Fichié déjà décompressé ! Déploiment en cours...")
    time.sleep(1)

else:
    with zipfile.ZipFile(folder + "/Client.zip","r") as zip_ref:
        zip_ref.extractall(folder + "/Client")
    time.sleep(1)


shutil.copytree(folder + "/Client/melonclient" ,minecraftDir + "/libraries/melonclient", dirs_exist_ok=True)
print("Librarie installée, installation de la version...")
time.sleep(1)

shutil.copytree(folder + "/Client/Melon Client" ,minecraftDir + "/versions/Melon Client", dirs_exist_ok=True)
print("Version installée, installation de Optifine !")

time.sleep(1)
print("Lancement de OptiFine_1.8.9_HD_U_M5.jar")

time.sleep(1)
subprocess.call(['java', '-jar', folder + '/CLient/OptiFine_1.8.9_HD_U_M5.jar'])

subprocess.call('cls', shell=True)

print("Installation terminée, cette fenêttre ce fermera dans 3 secondes.")
time.sleep(3)