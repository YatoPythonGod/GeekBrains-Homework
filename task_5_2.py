#* (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

def odd_nums(i):
    return (num for num in range(1, int(i)+1) if num % 2 == 0)


print(list(odd_nums(100)))
