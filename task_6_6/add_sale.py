import sys


def sale_ap(estimate):
    with open('task_6_6/bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{estimate}\n')


if __name__ == '__main__':
    try:
        sale_ap(sys.argv[1])
    except IndexError:
        print('Необходимо ввести один параметр')
