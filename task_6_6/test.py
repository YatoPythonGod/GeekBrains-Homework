import sys


def get_users_message_count():
    result = dict()
    with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            ip = line.partition(' - - ')[0]
            if result.get(ip) is None:
                result[ip] = 1
                continue
            else:
                result[ip] += 1
    return result


def show_spammer():
    sorted_users_dict = dict(sorted(get_users_message_count().items(), key=lambda x: x[1], reverse=True))
    print(next(iter(sorted_users_dict)))


show_spammer()