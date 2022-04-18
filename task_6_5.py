# **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
# задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.

from itertools import zip_longest
import sys


def grt_f_hobby(file_1, file_2, res_file):
    with open(file_1, encoding='utf-8') as f1, open(file_2, encoding='utf-8') as f2, open(res_file, 'w',
                                                                                          encoding='utf-8') as f3:
        user = [line.strip() for line in f1]
        hobby = [line.strip() for line in f2]
        result = zip_longest(user, hobby, fillvalue=None) if len(user) >= len(hobby) else sys.exit(1)

        for item in result:
            print(': '.join(item), file=f3)


if __name__ == '__main__':
    grt_f_hobby(sys.argv[1], sys.argv[2], sys.argv[3])
