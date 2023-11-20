from pathlib import Path
import re
import csv

def reader():
    path = 'parts_script_todo_finished.csv'
    tableau = []
    with open(path) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in spamreader:
            tableau.append(row)
    s = '{'
    for line in tableau:
        name = line[0]
        if line[1] == '#N/A' or len(name) == 0:
            s += f'\'{name}\': (10000, {line[2]}),\n'
        else:
            s += f'\'{name}\': ({line[1]}, {line[2]}),\n'
    s += '}'
    print(s)


reader()
