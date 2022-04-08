# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

import random


def get_jokes(count, repetition=True):
    """
    Making random jokes in list

    :param count: count jokes in list
    :param repetition=True: allows or disables the repetition of words in jokes,
     True value disables repetition
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    random.shuffle(adjectives)
    random.shuffle(nouns)
    random.shuffle(adverbs)
    if repetition:
        result = []
        for noun, adverb, adjective in zip(nouns, adverbs, adjectives):
            result.append(f'{noun} {adverb} {adjective}')
        return result[:count]
    else:
        result = []
        for i in range(count):
            result.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
        return result


print(get_jokes(7, False))
print(get_jokes(3))
