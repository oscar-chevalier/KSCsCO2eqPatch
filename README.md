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

## Construire le GameData
### Installation
Pour le moment le mod n'est pas packagé CKAN aussi la liste des mods constituant le GameData du concours
est la suivante. Nous vous recommandons de les installer via CKAN sauf mention contraire explicite.
- KSRSS et sa dépendance Kopernicus. Vous pouvez aussi installer Kronometer si le coeur vous en dit.
Attention KSRSS est à télécharger sur GitLab : https://gitlab.com/ksrss/KSRSS
- KSCSwitcher, pour que Kourou soit la base spatiale par défaut
- EVE, Scatterer
- Restock, Restock+, Restock RigidLegs
- KER, Trajectories
- Version spécifique de Transfer Window Planner qui permet de créer des alarmes dans le KAC stock du jeu :
https://github.com/yalov/TransferWindowPlanner/releases
- Il n'y avait pas les KSPCommunityFixes mais vous pouvez l'ajouter sans problème.
- et donc le contenu de GameData de ce présent mod

### Configuration 
Il y a 2 fichiers à modifier manuellement
GameData/KSRSS/Patches/KSRSS_LaunchSites.cfg
Modifier la ligne DefaultSite ainsi :
```@DefaultSite = fr_kourou
```
GameData/KSRSS/Configuration.cfg
Modifier la ligne SystemScale ainsi :
```SystemScale = Stock // Default, Stock
```

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

## Building your GameData
### Installation
At the moment the mod is not packaged with CKAN also the list of mods constituting the GameData of the competition
is the following. We recommend installing them via CKAN unless explicitly stated otherwise.
- KSRSS and its Kopernicus dependency. You can also install Kronometer if you feel like it.
Please note KSRSS can be downloaded from GitLab: https://gitlab.com/ksrss/KSRSS
- KSCSwitcher, so that Kourou is the default space base
- EVE, Scatterer
- Restock, Restock+, Restock RigidLegs
- KER, Trajectories
- Specific version of Transfer Window Planner which allows you to create alarms in the game's stock KAC:
https://github.com/yalov/TransferWindowPlanner/releases
- There was no KSPCommunityFixes but you can add it without problem.
- and therefore the GameData content of this present mod

### Configuration
There are 2 files to be manually updated 
- GameData/KSRSS/Patches/KSRSS_LaunchSites.cfg
DefaultSite line => 	@DefaultSite = fr_kourou
- GameData/KSRSS/Configuration.cfg
SystemScale line =>   SystemScale = Stock // Default, Stock

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
./insert_co2_script.sh  # Apply the modifications to the game
```

### Modification of ``calculate_empty.py``
```# Create "parts_script_todo.csv" from "Parts - parts_3_full_mass_price.csv"
python3 script_csv_translator.py  # Modify the name of the .cfg by the names use by the game
python3 dict_creator.py
# Edit "calculate_empty.py"
# Edit the cost of ressources
```
