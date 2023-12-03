from pathlib import Path
import re
import csv

Fu = 0.05
Ox = 0.05
So = 0.075
Mono = 0.04
Xenon = 0.001
Ore = 0.1
Ablator = 0.01

def reader(path):
    tableau = []
    with open(path) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in spamreader:
            tableau.append(row)
    return tableau


def add_price_full(tline):
    name = ''
    path = tline[-1]
    cost = 0
    etat = ''
    vFu = -1
    vOx = -1
    vSo = -1
    vMono = -1
    vXenon = -1
    vOre = -1
    vAblator = -1
    if path == '':
        print("IGNORED", tline)
        return
    with open(path) as read_file:
        for line in read_file:
            m = re.match(r'name.*= (?P<name>.+)', line.strip())
            if len(name) == 0 and m is not None:
                name = m['name']
    tline[0] = name



def csv_creator(parts):
    with open('parts_script_todo_finished.csv', mode='w') as csv_table:
        table_writer = csv.writer(csv_table, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, dialect='unix')
        for part in parts:
            table_writer.writerow(part)


def main():
    tableau = reader('parts_script_todo.csv')
    for line in tableau:
        print(line[0])
        add_price_full(line)
        print(line[0])
    csv_creator(tableau)
    
    

if __name__ == '__main__':
    main()
