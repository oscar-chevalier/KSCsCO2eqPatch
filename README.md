# Français
## Introduction
Tous ces outils ont été créé pour le KSPACECONTEST de 2023 organisé par Spacecon et KSC.
Cette chaîne d'outil modifie directement les fichiers du jeu (surtout les fichier ".cfg" des pièces).
L'objectif est d'appliquer un coût équivalent CO2 aux pièces.
Le règlement du concours est ici :
https://www.kerbalspacechallenge.fr/wp-content/uploads/2023/11/KSpaceContest_Requirements.pdf

## Attention ! Compatibilité Restreinte !
Le but de ce mod est de récréer des conditions équivalentes au KSPACECONTEST 2023 c'est à dire une
expérience de jeu particulière pour le mode Sandbox uniquement !
Ce mod change les prix des parts pour
- KSP Stock
- KSP DLCs (les deux)
- Restock+
- KER (oui les deux petites parts fournies avec le mod)
En aucune manière la compatibilité de ce mod avec le mode carrière existant n'a été voulue car
les contrats et la mécanique financière du jeu ne sont pas modifiés pour en tenir compte.
De la même manière aucune prise en compte de part mods autres que ceux listés plus haut est assurée.

Par ailleurs, et là c'est une nouveauté par rapport au KSPACECONTEST2023, nous avons fait les choses proprement.
A savoir que 4 pièces sont supprimées du jeu par notre mod :
- Le moteur stock nucléaire
- Le moteur Restock+ nucléaire
- Le RTG
- Le RTG des équipements scientifiques déployables du DLC Breaking Ground.

## Construire le GameData KSPACECONTEST 2023
### Installation
Pour le moment le mod n'est pas packagé CKAN aussi la liste des mods constituant le GameData du concours
est la suivante. Nous recommandons d'utiliser CKAN qui permet de gérer les dépendances.
Si vous n'utilisez pas CKAN, à vous de trouver quelle dépendance doit s'appliquer.

**1) Obligatoire**, avec CKAN, installez
- Kopernicus Planetary System Modifier
- Custom Barn Kit (dépendance de KSRSS)
- KSCSwitcher 
- KER,
- Restockplus & Restock Extra RigidLegs
- Trajectories

**2) Obligatoire**, manuellement, installez
- KSRSS, https://gitlab.com/ksrss/KSRSS. Sous le titre de la page vérifiez bien que "reborn" est séléctionné, puis en haut à droite
cliquez sur "Code" puis "download Zip". Une fois téléchargé ouvrez le zip et copiez KSRSS dans le GameData. Si vous avez une machine
dotée d'une carte vidéo un peu costaude en terme de VRAM (disons 8Gb), vous pouvez prendre aussi KSRSS-64k.
- Version spécifique de Transfer Window Planner qui permet de créer des alarmes dans le KAC stock du jeu :
https://github.com/yalov/TransferWindowPlanner/releases
- Notre patch trouvable dans nos releases https://github.com/oscar-chevalier/KSPACECONTEST23-tools/releases

**3) Facultatif**, avec CKAN, installez
- Si vous souhaitez une gestion du temps à la RSS, installez Kronometer
- EVE, Scatterer, PlanetShine, DistantObjectEnhancement, Waterfall core, Waterfall Restock voire RealPlume pour les boosters à poudre
Choisissez les versions stocks des fichiers de configuration si CKAN vous les demande (ex EVE: Stock Planet Config Files).
KSRSS les patchera si nécessaire.
- Nous recommandons chaudement d'installer KSPCommunityFixes 

## Les outils, leur utilisation
### Précisions
Tous les CSV sont séparé par des ";".
Cette chaîne d'outils est faite pour fonctionner sur une distribution Linux avec Python3.

### Modification des fichiers du jeu
```python3 translator.py
cp parts.csv parts_2.csv
# Éditer parts2.csv avec le CO2, format du csv : "X;X;X;.cfg;CO2;prix;masse;X;chemin"
# Éditer le nom du fichier édité "Parts - parts_3_full_mass_price.csv"
python3 addfuel.py
./insert_co2_script.sh  # Applique les modifications au jeu
```

### Modification de ``calculate_empty.py``
```# Créer "parts_script_todo.csv" à partir de "Parts - parts_3_full_mass_price.csv"
python3 script_csv_translator.py  # Modifie les noms de .cfg pour le nom utilisé par le jeu
python3 dict_creator.py
# Éditer "calculate_empty.py"
# Éditer le prix des ressources
```

# English
## Introduction
This tools were created for the KSPACECONTEST23 organised by Spacecon and KSC.
This tool chain directly modify the game files (mainly the parts' files ".cfg").
The objective is to apply a cost of equivalent CO2 to the parts.
The rules of the contest are here:
https://www.kerbalspacechallenge.fr/wp-content/uploads/2023/12/KSpaceContest-Requirements-en-version.pdf

## Warning! Limited Compatibility!
The purpose of this mod is to reproduce the specific conditions players encountered for the
KSPACECONTEST 2023: a specific game experience for a Sandbox Game!
This mod alters the price of parts for
- KSP Stock
- KSP DLCs (both)
- Restock+
- KER (yes, the 2 little parts provided with this mod)
In no way was the compatibility of this mod with the existing career mode intended because
contracts and the financial mechanics of the game are not modified accordingly.
In the same way, no consideration of part mods other than those listed above is ensured.

## Building the KSPACECONTEST2003 GameData
### Installation
At the moment the mod is not packaged CKAN also the list of mods constituting the GameData of the competition
is the following. We recommend using CKAN which allows you to manage dependencies.
If you are not using CKAN, it is up to you to figure out which dependency should apply.

**1) Mandatory**, with CKAN, install
- Kopernicus.
- KSCSwitcher
- KER,
- Restockplus, Restockplus RigidLegs
- Trajectories

**2) Mandatory**, manually, install
- KSRSS, https://gitlab.com/ksrss/KSRSS choose reborn
- Specific version of Transfer Window Planner which allows you to create alarms in the game's stock KAC:
https://github.com/yalov/TransferWindowPlanner/releases
- Our patch found in our releases https://github.com/oscar-chevalier/KSPACECONTEST23-tools/releases

**3) Optional**, with CKAN, install
- If you want a RSS like time management, install Kronometer
- EVE, Scatterer, PlanetShine, DistantObjectEnhancement, Waterfall core, Waterfall Restock or even RealPlume for powder boosters
- We highly recommend installing KSPCommunityFixes


## The Tools used, and how to use them
### Precisions
All the CSV are ";" separated.
This tool chain is made to work on Linux with Python3.

### Modification of the game files
```python3 translator.py
cp parts.csv parts_2.csv
# Edit parts2.csv with the CO2, csv format : "X;X;X;.cfg;CO2;cost;mass;X;path"
# Edit the name of the edited file "Parts - parts_3_full_mass_price.csv"
python3 addfuel.py
./insert_co2_script.sh  # Apply the modifications to the game
```

### Modification of ``calculate_empty.py``
```# Create "parts_script_todo.csv" from "Parts - parts_3_full_mass_price.csv"
python3 script_csv_translator.py  # Modify the name of the .cfg by the names use by the game
python3 dict_creator.py
# Edit "calculate_empty.py"
# Edit the cost of ressources
```
