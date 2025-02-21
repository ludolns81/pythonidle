import sys
import os
import subprocess

# Récupère le chemin d'installation de Python depuis l'utilisateur actuel
USER = os.environ.get("USERNAME")  # Récupère le nom d'utilisateur Windows
PYTHON_PATH = fr"C:\Users\{USER}\AppData\Local\Programs\Python\Python311"
IDLE_PATH = os.path.join(PYTHON_PATH, "Lib", "idlelib", "idle.pyw")
PYTHONW_EXEC = os.path.join(PYTHON_PATH, "pythonw.exe")

# Vérifie si Python et IDLE existent
if not os.path.isfile(IDLE_PATH):
    print(f"Erreur : idle.pyw introuvable à {IDLE_PATH}")
    sys.exit(1)

# Construire la commande pour exécuter IDLE
command = [PYTHONW_EXEC, IDLE_PATH]

# Ajouter le fichier Python à ouvrir si fourni
if len(sys.argv) > 1:
    command.append(sys.argv[1])

# Exécuter la commande
try:
    subprocess.run(command, check=True)
except FileNotFoundError:
    print("Erreur : Pythonw.exe ou IDLE introuvable")


