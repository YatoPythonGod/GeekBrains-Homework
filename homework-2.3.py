# 3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.

new_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for item in new_list[:]:
    if item.replace('+', '').replace('.', '').replace('-', '').isdigit():
        n = 2
        for j in item:
            if j in ['-', '+']:
                n += 1
            elif j == '.':
                n += len(item[item.index(j):])
        new_list.insert(new_list.index(item), '"')
        new_list.insert(new_list.index(item) + 1, '"')
        new_list[new_list.index(item)] = item.zfill(n)

print(new_list)

# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

while '"' in new_list:
    new_list.remove('"')

result_str = ' '.join(
    '"' + item + '"' if item.replace('+', '').replace('.', '').replace('-', '').isdigit() else item for item in
    new_list)

print(result_str)
