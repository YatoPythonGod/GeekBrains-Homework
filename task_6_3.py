# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
# и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
# в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
# записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
# скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
# меньше объема ОЗУ

from itertools import zip_longest
import sys
import pickle

with open('users.csv', encoding='utf-8') as f1, open('hobby.csv', encoding='utf-8') as f2, open('result_6_3.csv',
                                                                                                'wb') as f3:
    user = [line.replace(',', ' ').strip() for line in f1]
    hobby = [line.strip() for line in f2]
    result = {k: v if len(user) >= len(hobby) else sys.exit(1) for k, v in zip_longest(user, hobby, fillvalue=None)}

    f3.write(pickle.dumps(result))

with open('result_6_3.csv', 'rb') as f:
    print(pickle.loads(f.read()))
