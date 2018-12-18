import fileinput
from pathlib import Path


def replace(file):
    for line in fileinput.input([file], inplace=True):
        print(line.replace('°C', 'dgr'), end='')
        print(line.replace('∞C', 'dgr'), end='')


path_list = Path('original_records').glob('**/*.txt')
for path in path_list:
    # because path is object not string
    path_in_str = str(path)
    print(path_in_str)
    replace(path_in_str)

