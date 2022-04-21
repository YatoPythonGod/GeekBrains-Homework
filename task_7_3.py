import os
import shutil
import sys


def add_temp_dir(project='my_project'):
    root_dir = os.path.join(os.getcwd(), project)
    if os.path.isdir(root_dir):
        result_dir = os.path.join(root_dir, 'templates')

        for root, dirs, files in os.walk(root_dir):
            if dirs == ['templates'] and os.path.join(root, 'templates') != result_dir:
                temp_root = os.path.join(root, 'templates')

                for root, dirs, files in os.walk(temp_root):
                    for file in files:
                        file_root = os.path.join(root, file)
                        split_file_root = os.path.split(file_root)
                        rel_root = os.path.relpath(split_file_root[0], temp_root)
                        root_new_dir = (os.path.join(result_dir, rel_root))
                        if not os.path.isdir(root_new_dir):
                            print(os.path.join(result_dir, rel_root))
                            os.makedirs(root_new_dir)
                        shutil.copy(file_root, os.path.join(root_new_dir, split_file_root[1]))
    else:
        print('Не найдена директория проекта')


if __name__ == '__main__':
    try:
        name_project = sys.argv[1]
        add_temp_dir(name_project)
    except IndexError:
        add_temp_dir()
        print('Операция выполнена в проекте - "my_project"')
