from pathlib import Path
import re
import csv

Fu = 0.8
MFu = 5/1000
Ox = 0.18
MOx = 5/1000
So = 0.6
MSo = 7.5/1000
Mono = 1.2
MMono = 4/1000
Xenon = 4
MXenon = 0.1/1000
Ore = 0.02
MOre = 10/1000
Ablator = 0.5
MAblator = 1/1000



class Part:
    def __init__(self, name, p, parents, cost, mass):
        self.name = name
        self.p = p
        self.cost = cost
        self.mass = mass
        self.parents = parents
    
    def __repr__(self):
        return f'{self.name}: {self.parents} ({self.cost})'


def rec(p, parents, files):
    for f in p.iterdir():
        if f.name[-4:] == '.cfg':
            files.append((f, parents))
        elif Path.is_dir(f) and f.name != 'Kerbal Space Program':
            p = parents[:]
            p.append(f.name)
            rec(f, p, files)
        else:
            print("refused", f.name)


def csv_creator(parts):
    with open('parts.csv', mode='w') as csv_table:
        table_writer = csv.writer(csv_table, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, dialect='unix')
        for part in parts:
            l = [part.name, part.cost, part.mass, part.parents, part.p]
            table_writer.writerow(l)


def parse(f, parents):
    name = f.name
    cost = -1
    mass = -1
    etat = ''
    vFu = -1
    vOx = -1
    vSo = -1
    vMono = -1
    vXenon = -1
    vOre = -1
    vAblator = -1
    print('=', f.name)
    with f.open() as read_file:
        for line in read_file:
            m = re.match(r'cost.*=[^0-9]*(?P<cost>\d+)', line.strip())
            n = re.match(r'mass.*=[^0-9]*(?P<mass>[\.0-9]+)', line.strip())
            if n is not None and mass == -1:
                mass = float(n['mass'])
            if m is not None:
                if cost != -1:
                    print('error', f.name, parents, line)
                    continue
                cost = int(m['cost'])
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
                cost -= Fu * float(m['amount'])
                if vFu == -1:
                    vFu = float(m['amount'])
            elif etat == 'Ox' and m is not None:
                cost -= Ox * float(m['amount'])
                if vOx == -1:
                    vOx = float(m['amount'])
            elif etat == 'So' and m is not None:
                cost -= So * float(m['amount'])
                if vSo == -1:
                    vSo = float(m['amount'])
            elif etat == 'Mono' and m is not None:
                cost -= Mono * float(m['amount'])
                if vMono == -1:
                    vMono = float(m['amount'])
            elif etat == 'Xenon' and m is not None:
                cost -= Xenon * float(m['amount'])
                if vXenon == -1:
                    vXenon = float(m['amount'])
            elif etat == 'Ore' and m is not None:
                cost -= Ore * float(m['amount'])
                if vOre == -1:
                    vOre = float(m['amount'])
            elif etat == 'Ablator' and m is not None:
                cost -= Ablator * float(m['amount'])
                if vAblator == -1:
                    vAblator = float(m['amount'])
            if '}' in line:
                etat = ''
            print(etat, cost, mass, line.strip())
    if vOre > 0:
        mass -= MOre * vOre
    if cost > 0:
        print(f'cmass{mass}, vFu = {vFu} vOx = {vOx}, vSo = {vSo} vMono = {vMono} vXenon = {vXenon} vOre = {vOre} vAblator = {vAblator}')
        return Part(name, f, parents, cost, mass)
    else:
        print(f'fmass{mass}')
    return None
            

def main():
    p = Path.cwd()
    print(p.name)
    files = []
    rec(p, [], files)
    print("len(files):", len(files))
    print("files:", files)
    parts = []
    for f, parents in files:
        print("enum", len(parts), f, parents)
        pa = parse(f, parents)
        if pa is not None:
            parts.append(pa)
    print(len(parts))
    print(parts)
    csv_creator(parts)
        
    
    

if __name__ == '__main__':
    main()
