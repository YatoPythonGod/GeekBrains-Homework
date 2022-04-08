# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
print('#1')
prices = [57.8, 46.51, 97, 222.34, 130.23, 55.5, 22.5, 32.8, 87.6, 100, 150.05, 5]
result_prices = [f'{price:.2f}' for price in prices]
result_str = ''
for price in result_prices:
    result_price = price.split('.')
    result_str += f'{result_price[0]} руб {result_price[1]} коп, '

result_str = result_str[:-2]

print(result_str)

# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).

print('#2')
print('Объект списка до сортировки:', id(prices))
prices.sort()
print('Объект списка после сортировки:', id(prices))

result_prices = [f'{price:.2f}' for price in prices]
result_str = ''

for price in result_prices:
    result_price = price.split('.')
    result_str += f'{result_price[0]} руб {result_price[1]} коп, '

result_str = result_str[:-2]

print(result_str)

# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
print('#3')
prices_reverse = sorted(prices, reverse=True)
print(prices_reverse)

result_prices = [f'{price:.2f}' for price in prices_reverse]
result_str = ''

for price in result_prices:
    result_price = price.split('.')
    result_str += f'{result_price[0]} руб {result_price[1]} коп, '

result_str = result_str[:-2]
print(result_str)

# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
print('#4')

top5 = ''
result_prices.reverse()
for price in result_prices[-5:]:
    result_price = price.split('.')
    top5 += f'{result_price[0]} руб {result_price[1]} коп, '
top5 = top5[:-2]

print('Цены 5 самых дорогих товаров:', top5)
