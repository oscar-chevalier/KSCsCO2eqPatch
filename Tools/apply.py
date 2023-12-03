"""
AUTHOR: Oscar Chevalier
WITH THE HELP: Only Light Matters
This is the file used to translate a Sheet to CFG files
"""

import csv
import sys
from typing import List, Dict


class Datas:
    def __init__(self, part_csv_path: str):
        self.part_csv_path: str = part_csv_path
        self.files: Dict[str, List[str]] = {}


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def add_part(datas: Datas, filename: str, mod: str, partname: str, tco2: float) -> bool:
    if filename not in datas.files:
        datas.files[filename] = []
    file: List[str] = datas.files[filename]
    pref: str = '@'
    if tco2 < 0:
        pref = '!'
    need: str = ''
    if mod not in 'squad':
        need += f':NEEDS[{mod}]'
    file.append(f'{pref}PART[{partname}]{need}:FOR[KSCsCO2eqPatch]')
    file.append('{')
    if tco2 >= 0:
        file.append(f'\t@cost = {tco2}')
    file.append('}')
    return True


def process_part(datas: Datas, line: List[str]) -> bool:
    index_value: Dict[str, int] = {'Partname': 3,
                                   'Mod': 4,
                                   'Tco$': 7}
    if len(line) <= max(index_value.values()):
        eprint(f'Failed to process the part {line}, expected {max(index_value.values()) + 1}'
               f'arguments, got {len(line)} arguments.')
        return False
    try:
        tco2: float = float(line[index_value['Tco$']])
    except ValueError:
        tco2: float = -1
    partname: str = line[index_value['Partname']]
    filename: str = line[index_value['Mod']]
    mod: str = filename
    if tco2 < 0:
        filename += '_remove'
    else:
        filename += '_add'
    return add_part(datas, filename, mod, partname, tco2)


def process_csv(datas: Datas) -> bool:
    try:
        csv_array: List[List[str]] = []
        with open(datas.part_csv_path) as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in spamreader:
                csv_array.append(row)
        for line in csv_array[1:]:  # First line is just the name of the columns
            process_part(datas, line)
    except UnicodeDecodeError:
        eprint(f'Failed to open {datas.part_csv_path}.')
        return False
    return True


def name_generator(namefile: str) -> str:
    return f'KSCsCO2eqPatch_{namefile}.cfg'


def write_single_file(namefile: str, file: List[str]) -> bool:
    with open(name_generator(namefile), 'w') as writing_file:
        for line in file:
            writing_file.write(line)
            writing_file.write('\n')
    return True


def write_files(datas: Datas) -> bool:
    for namefile, file in datas.files.items():
        if not write_single_file(namefile, file):
            eprint(f'Failed to write in the file {namefile}.')
            return False
    return True


def main() -> bool:
    part_csv_part: str = input('Csv table path: ')
    datas: Datas = Datas(part_csv_part)
    if process_csv(datas):
        return write_files(datas)
    eprint('Failed to process the csv.')
    return False


if __name__ == '__main__':
    main()
