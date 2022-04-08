# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(),
# принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
# в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания
# и содержащие записи, в которых фамилия начинается с соответствующей буквы.
# Как поступить, если потребуется сортировка по ключам?

def thesaurus(*args):
    thesaurus = {}

    for item in args:
        new_list = item.split(' ')
        thesaurus[new_list[-1][0]] = thesaurus.get(new_list[-1][0], dict())
        thesaurus.get(new_list[-1][0]).update(dict([(new_list[0][0], item)]))

    sort_thesaurus = dict(sorted(thesaurus.items()))

    for key, val in sort_thesaurus.items():
        sort_value = dict(sorted(val.items()))
        sort_thesaurus[key] = sort_value

    return sort_thesaurus


print(thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
