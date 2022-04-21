import os
import sys
import json
from collections import defaultdict


def get_data(name_folder='some_data'):
    data_files = defaultdict(list)
    proj_root = os.path.join(os.getcwd(), name_folder)
    for root, dirs, files in os.walk(proj_root):
        n = 0
        for file in files:
            n += 1
            ext = file.rsplit('.', maxsplit=1)[1]
            data_files[str(10 ** len(str(os.stat(os.path.join(root, file)).st_size)))].append(ext)
    result = {}
    for k, v in data_files.items():
        result[k] = (len(v), list(set(v)))
    try:
        with open(f'{name_folder}_summary.json', 'x', encoding='utf-8') as f:
            str_result = json.dumps(result)
            f.write(str_result)
    except FileExistsError:
        print(f'Файл {name_folder}_summary.json уже существует')


if __name__ == '__main__':
    try:
        folder = sys.argv[1]
        get_data(folder)
    except IndexError:
        print('Выполняется операция для директории - "some_data"')
        get_data()
