import re


class MyValErr(Exception):
    pass


my_lst = []
num_format = re.compile(r'[+-]?\d+(?:\.\d+)?')

while True:
    try:
        el = input('Enter number: ')
        if el == 'stop':
            break
        elif re.match(num_format, el):
            my_lst.append(int(el))
        else:
            raise MyValErr(f'{el} - is not number!')
    except MyValErr as err:
        print(err)

print(my_lst)
