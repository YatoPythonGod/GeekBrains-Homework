import os
import json
import sys


def write_file(content, blank='blank_project.json'):
    with open(blank, 'x', encoding='utf-8') as f:
        content_str = json.dumps(content)
        f.write(content_str)


def load_file(blank='blank_project.json'):
    with open(blank, 'r', encoding='utf-8') as f:
        str_blank = f.read()
        return json.loads(str_blank)


def greate_dir(dict_proj, root=os.getcwd()):
    for fldr, sub_fldr in dict_proj.items():
        try:
            dir_path = os.path.join(root, fldr)
            if fldr == '__files__':
                for item in sub_fldr:
                    with open(os.path.join(os.path.dirname(dir_path), item), 'w'): pass
                continue
            elif not os.path.isdir(fldr):
                os.mkdir(dir_path)
                if isinstance(sub_fldr, dict):
                    greate_dir(sub_fldr, root=os.path.join(os.path.join(root, fldr)))

        except AttributeError:
            return


if __name__ == '__main__':
    try:
        stand_blank_project = {'my_project': {'settings': {}, 'mainapp': {}, 'adminapp': {}, 'authapp': {}}}
        write_file(stand_blank_project)
    except FileExistsError:
        pass

    try:
        new_blank = load_file(sys.argv[1])
        greate_dir(new_blank)
    except IndexError:
        print('Создан стандартный стартер проекта "my_project"')
        stand_blank_project = load_file()
        greate_dir(stand_blank_project)
