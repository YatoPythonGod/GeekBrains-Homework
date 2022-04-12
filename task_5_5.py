# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном
# списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

rep_num = set()
uniq_num = set()

for el in src:
    if el in rep_num:
        continue
    if el in uniq_num:
        uniq_num.discard(el)
        rep_num.add(el)
        continue
    uniq_num.add(el)

result = [el for el in src if el in uniq_num]

print(result)
