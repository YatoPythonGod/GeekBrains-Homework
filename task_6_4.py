# *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём
# ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на
# будущее проекта). Только теперь не нужно создавать словарь с данными. Вместо этого нужно
# сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через
# двоеточие и пробел после ФИО:

from itertools import zip_longest
import sys

with open('users.csv', encoding='utf-8') as f1, open('hobby.csv', encoding='utf-8') as f2, open('users_hobby.txt', 'w',
                                                                                                encoding='utf-8') as f3:
    user = [line.strip() for line in f1]
    hobby = [line.strip() for line in f2]
    result = zip_longest(user, hobby, fillvalue=None) if len(user) >= len(hobby) else sys.exit(1)

    for item in result:
        print(': '.join(item), file=f3)
