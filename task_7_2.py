import os
import json
from task_7_1 import write_file
from task_7_1 import load_file
from task_7_1 import greate_dir

my_dir = {'my_project':
              {'settings': {'__files__': ['__init__.py', 'dev.py', 'prod.py']},
               'mainapp':
                   {'templates':
                        {'mainapp': {'__files__': ['base.html', 'index.html']}}},
               'authapp':
                   {'__files__': ['__init__.py', 'models.py', 'views.py'],
                    'templates':
                        {'authapp': {'__files__': ['base.html', 'index.html']}}
                    }}}

if __name__ == '__main__':
    file = 'config.json'
    try:
        write_file(my_dir, file)
    except FileExistsError:
        pass
    fin_dir = load_file(file)
    greate_dir(fin_dir)
