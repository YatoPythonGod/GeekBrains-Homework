import re


def email_parse(email):
    text = email
    pattern = re.compile(r'^\b(?P<username>[A-z0-9.-]+)\b@\b(?P<domain>[a-z]+[.][A-z]{2,3})\b')
    if pattern.match(text):
        return pattern.match(text).groupdict()
    else:
        raise ValueError(f'wrong email: {email}')


print(email_parse('someone@geekbrains.ru'))
