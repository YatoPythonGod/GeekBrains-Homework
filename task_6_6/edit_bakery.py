import sys


def edit_f(num_line, value):
    with open('task_6_6/bakery.csv', 'r+', encoding='utf-8') as f:
        count = 0
        for _ in f:
            count += 1
        if count < num_line or num_line <= 0:
            print('Номер записи не существует!')
            return

        f.seek(0)
        for i in range(num_line-1):
            f.readline()
        cursor = f.tell()
        req_len = len(f.readline())
        sec_part = f.read()
        f.seek(cursor)
        f.write(f'{str(value).ljust(req_len - 1)}\n{sec_part}')


if __name__ == '__main__':
    try:
        req_str = int(sys.argv[1])
        req_sum = sys.argv[2]
    except IndexError:
        print('Отсутствует номер строки и/или cумма продаж')
    except ValueError:
        print('Неверный ввод номера строки. Введите целое число.')
    else:
        edit_f(req_str, req_sum)
