# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

new_list = []

for i in range(1, 1000):
    if i % 2 != 0:
        i = i ** 3
        new_list.append(i)

print(new_list)

result = 0
for i in new_list:
    i = str(i)
    zero = len(str(i)) - 1
    if zero == 0:
        i = int(i)
        if i % 7 == 0:
            result = result + i
    if zero != 0:
        n = '1' + zero * '0'
        n = int(n)
        sum_i = int(i) // n
        for j in range(zero - 1):
            sum_i = sum_i + ((int(i) % n) // (n / 10))
            n = n / 10
        sum_i = sum_i + (int(i) % 10)
        if sum_i % 7 == 0:
            result = result + int(i)

print(result)

# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

result = 0

for i in new_list:
    i = i + 17
    i = str(i)
    zero = len(str(i)) - 1
    if zero == 0:
        i = int(i)
        if i % 7 == 0:
            result = result + i
    if zero != 0:
        n = '1' + zero * '0'
        n = int(n)
        sum_i = int(i) // n
        for j in range(zero - 1):
            sum_i = sum_i + ((int(i) % n) // (n / 10))
            n = n / 10
        sum_i = sum_i + (int(i) % 10)
        if sum_i % 7 == 0:
            result = result + int(i)

print(result)
