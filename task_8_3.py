from functools import wraps


def type_logger(callback):
    @wraps(callback)
    def wrapper(*args, **kwargs):
        arg_n_type = []
        for arg in args:
            arg_n_type.append(f'{str(arg)}: {type(arg)}')
        for k, v in kwargs.items():
            arg_n_type.append(f'{str(k)}={str(v)}: {type(v)}')
        msg = ', '.join(arg_n_type)
        print(f'{callback.__name__}({msg})')
        result = callback(*args, **kwargs)
        return result

    return wrapper


@type_logger
def calc_cube(x):
    """Calculates cube area"""
    return x ** 3


@type_logger
def calc_triangle_area(h=10, b=5):
    return 0.5 * b * h


print(calc_cube(5))
print(calc_triangle_area(h=5, b=5))
help(calc_cube)
