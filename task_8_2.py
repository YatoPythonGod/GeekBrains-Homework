import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        pattern = re.compile(
            r'^([0-9.]+)\s-\s-\s\[([A-z0-9/:]+\s\+\d{4})\]\s\"([A-z]+)\s([A-z/0-9.]+)\s[A-z0-9./]+\"\s(\d{3})\s(\d+)')
        if pattern.match(line):
            print(pattern.match(line).groups())
        else:
            pattern = re.compile(
                r'^([a-z0-9.:]+)\s-\s-\s\[([A-z0-9/:]+\s\+\d{4})\]\s\"([A-z]+)\s([A-z/0-9.]+)\s[A-z0-9./]+\"\s(\d{3})\s(\d+)')
            print(pattern.match(line).groups())
