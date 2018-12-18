import os
from os import rename, listdir


def get_subdirectories(dir):
    directories = ([name for name in os.listdir(dir) if os.path.isdir(os.path.join(dir, name))])
    for n in directories:
        rename_files(n)


def rename_files(a_dir):
    file_names = listdir('output/original_records/%s' % a_dir)
    print(file_names)

    for file_name in file_names:
        print(file_name)
        rename('output/original_records/%s/%s' % (a_dir, file_name), 'output/original_records/%s/%s-%s' % (a_dir, a_dir, file_name))


get_subdirectories('output/original_records')
