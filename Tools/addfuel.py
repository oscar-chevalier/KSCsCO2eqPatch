from pathlib import Path
import re
import csv

Fu = 0.05
Ox = 0.05
So = 0.075
Mono = 0.04
Xenon = 0.01
Ore = 0.1
Ablator = 0.01

def reader(path):
    tableau = []
    with open(path) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in spamreader:
            tableau.append(row)
    for line in tableau:
        if line[0] == 'NULL':
            line[4] = 10000
        else:
            line[4] = float(line[4])
    return tableau


def add_price_full(tline):
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
            m = re.match(r'name.*=.*LiquidFuel', line.strip())
            if m is not None:
                etat = 'Fu'
            m = re.match(r'name.*=.*Oxidizer', line.strip())
            if m is not None:
                etat = 'Ox'
            m = re.match(r'name.*=.*MonoPropellant', line.strip())
            if m is not None:
                etat = 'Mono'
            m = re.match(r'name.*=.*SolidFuel', line.strip())
            if m is not None:
                etat = 'So'
            m = re.match(r'name.*=.*XenonGas', line.strip())
            if m is not None:
                etat = 'Xenon'
            m = re.match(r'name.*=.*Ore', line.strip())
            if m is not None:
                etat = 'Ore'
            m = re.match(r'name.*=.*Ablator', line.strip())
            if m is not None:
                etat = 'Ablator'
            m = re.match(r'maxAmount.*=[^0-9]*(?P<amount>\d+)', line.strip())
            if etat == 'Fu' and m is not None:
                cost += Fu * float(m['amount'])
                if vFu == -1:
                    vFu = float(m['amount'])
            elif etat == 'Ox' and m is not None:
                cost += Ox * float(m['amount'])
                if vOx == -1:
                    vOx = float(m['amount'])
            elif etat == 'So' and m is not None:
                cost += So * float(m['amount'])
                if vSo == -1:
                    vSo = float(m['amount'])
            elif etat == 'Mono' and m is not None:
                cost += Mono * float(m['amount'])
                if vMono == -1:
                    vMono = float(m['amount'])
            elif etat == 'Xenon' and m is not None:
                cost += Xenon * float(m['amount'])
                if vXenon == -1:
                    vXenon = float(m['amount'])
            elif etat == 'Ore' and m is not None:
                cost += Ore * float(m['amount'])
                if vOre == -1:
                    vOre = float(m['amount'])
            elif etat == 'Ablator' and m is not None:
                cost += Ablator * float(m['amount'])
                if vAblator == -1:
                    vAblator = float(m['amount'])
            if '}' in line:
                etat = ''
    print(f'cost = {cost} vFu = {vFu} vOx = {vOx}, vSo = {vSo} vMono = {vMono} vXenon = {vXenon} vOre = {vOre} vAblator = {vAblator}')
    tline[4] += cost



def csv_creator(parts):
    with open('parts_to_insert.csv', mode='w') as csv_table:
        table_writer = csv.writer(csv_table, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, dialect='unix')
        for part in parts:
            table_writer.writerow(part)


def main():
    tableau = reader('Parts - parts_3_full_mass_price.csv')
    for line in tableau:
        print(line[4])
    for line in tableau:
        print(line)
        print(line[4])
        add_price_full(line)
        print(line[4])
    csv_creator(tableau)
    
    

if __name__ == '__main__':
    main()
