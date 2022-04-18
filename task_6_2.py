# 2. Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.

with open('nginx_logs.txt', encoding='utf-8') as f:
    ip_dict = dict()
    for line in f:
        ip_dict[line.partition(' ')[0]] = ip_dict.get(line.partition(' ')[0], 0) + 1

    result = max(ip_dict, key=ip_dict.get)

    print(f'IP: {result}\nКоличество запросов: {ip_dict.get(result)}')
