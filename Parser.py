import os
from pathlib import Path


def main(current_path):
    data = []
    date = 1
    current_row = 0

    with open(current_path, 'r') as file:
        next(file)  # skip headings
        import csv
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            data.append(row)

    number_rows = len(data)
    current_strain = data[current_row][1]
    os.makedirs(os.path.dirname('separated_records/%s/' % current_path[:-4]), exist_ok=True)
    new_file = open("separated_records/%s/%s.txt" % (current_path[:-4], current_strain), "w+")

    while current_row <= number_rows:
        current_strain = data[current_row][1]
        current_death = data[current_row][3]

        if current_row < number_rows - 1:
            next_strain = data[current_row + 1][1]
        else:
            return 0

        if next_strain == current_strain:
            new_file.write("%s\t%s\t%s\n" % (date, current_strain, current_death))
            current_row += 1
            date += 1
        else:
            new_file.write("%s\t%s\t%s\n" % (date, current_strain, current_death))
            new_file = open("separated_records/%s/%s.txt" % (current_path[:-4], next_strain), "w+")
            current_row += 1
            date = 1


path_list = Path('original_records').glob('**/*.txt')
for path in path_list:
    # because path is object not string
    path_in_str = str(path)
    print(path_in_str)
    main(path_in_str)
