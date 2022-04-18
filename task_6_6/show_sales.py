import sys


def sale_r(start=None, end=None):
    with open('task_6_6/bakery.csv', 'r', encoding='utf-8') as f:
        if start and end:
            for num, line in enumerate(f):
                if int(start) <= num + 1 <= int(end):
                    print(line.strip())
        elif start:
            for num, line in enumerate(f):
                if int(start) <= num + 1:
                    print(line.strip())
        else:
            print(f.read())


if __name__ == '__main__':
    try:
        sale_r(start=sys.argv[1], end=sys.argv[2])
    except IndexError:
        try:
            sale_r(start=sys.argv[1])
        except IndexError:
            sale_r()
