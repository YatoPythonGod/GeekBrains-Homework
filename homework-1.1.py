### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input('Введите кол-во секунд: '))
if duration < 60:
    print(f'{duration} cек')
elif duration >= 60 and duration < 3600:
    print(f'{duration // 60} мин {duration % 60} cек')
elif duration >= 3600 and duration < 3600 * 24:
    print(f'{duration // 3600} час {(duration % 3600) // 60} мин {duration % 60} сек ')
elif duration >= 3600 * 24:
    print(
        f'{duration // (3600 * 24)} дн {(duration % (3600 * 24)) // 3600} час {(duration % 3600) // 60} мин {duration % 60} сек ')
