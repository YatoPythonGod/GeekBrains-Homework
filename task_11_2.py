class MyZeroErr(Exception):
    pass


def division():
    x = int(input('Enter divided: '))

    try:
        y = int(input('Enter divisor: '))
        if y == 0:
            raise MyZeroErr('Error! Divisor zero!')
    except MyZeroErr as err:
        print(err)
        division()
    else:
        print(x / y)


division()
