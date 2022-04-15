# Есть два списка. Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)

from itertools import zip_longest
from sys import getsizeof

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

tut_n_class = zip_longest(tutors, classes, fillvalue=None) if len(tutors) > len(classes) else zip(tutors, classes)

# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
print(f'Тип объекта: {type(tut_n_class)}')
print(f'Размер объекта: {getsizeof(tut_n_class)}')
print(next(tut_n_class))
print(next(tut_n_class))
print(*tut_n_class)
