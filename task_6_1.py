# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
# web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>,
# <requested_resource>).

with open('nginx_logs.txt', encoding='utf-8') as f:
    result = [(line.partition(' ')[0], line.partition('"')[2][:3], line.partition('GET ')[2][:20]) for line in f]
    print(result[:10])  # для примера вывел первые 10 кортежей
