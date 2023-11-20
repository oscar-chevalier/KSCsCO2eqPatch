# Français
## Introduction
Tous ces outils ont été créé pour le KSPACECONTEST de 2023 organisé par Spacecon et KSC.
Cette chaîne d'outil modifie directement les fichiers du jeu (surtout les fichier ".cfg" des pièces).
L'objectif est d'appliquer un coût équivalent CO2 aux pièces.

## Utilisation
### Précisions
Tous les CSV sont séparé par des ";".
Cette chaîne d'outils est faite pour fonctionner sur une distribution Linux avec Python3.

### Modification des fichiers du jeu
```python3 translator.py
cp parts.csv parts_2.csv
# Éditer parts2.csv avec le CO2, format du csv : "X;X;X;.cfg;CO2;prix;masse;X;chemin"
# Éditer le nom du fichier édité "Parts - parts_3_full_mass_price.csv"
python3 addfuel.py
./insert_co2_script.sh  # Applique les modifications au jeu```

### Modification de ``calculate_empty.py``
```# Créer "parts_script_todo.csv" à partir de "Parts - parts_3_full_mass_price.csv"
python3 script_csv_translator.py  # Modifie les noms de .cfg pou le nom utilisé par le jeu
python3 dict_creator.py
# Édtier "calculate_empty.py"
# Édtier le prix des ressources```

# English
## Introduction
This tools were created for the KSPACECONTEST23 organised by Spacecon and KSC.
This tool chain directly modify the game files (mainly the parts' files ".cfg").
The objective is to apply a cost of equivalent CO2 to the parts.

## Use
### Précisions
All the CSV are ";" separated.
This tool chain is made to work on Linux with Python3.

### Modification of the game files
```python3 translator.py
cp parts.csv parts_2.csv
# Edit parts2.csv with the CO2, csv format : "X;X;X;.cfg;CO2;cost;mass;X;path"
# Edit the name of the edited file "Parts - parts_3_full_mass_price.csv"
python3 addfuel.py
./insert_co2_script.sh  # Apply the modifications to the game```

### Modification of ``calculate_empty.py``
```# Create "parts_script_todo.csv" from "Parts - parts_3_full_mass_price.csv"
python3 script_csv_translator.py  # Modify the name of the .cfg by the names use by the game
python3 dict_creator.py
# Edit "calculate_empty.py"
# Edit the cost of ressources```
