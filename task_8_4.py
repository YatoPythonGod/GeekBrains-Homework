from functools import wraps


def val_checker(validation):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if not validation(arg):
                    raise ValueError(f'wrong val {arg}')
            for k, v in kwargs.items():
                if not validation(v):
                    raise ValueError(f'wrong val {v}')
            result = func(*args, **kwargs)
            return result

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    """Calculates cube area"""
    return x ** 3


@val_checker(lambda x: x > 0)
def calc_triangle_area(h=10, b=5):
    return 0.5 * b * h


print(calc_cube(5))
print(calc_triangle_area(h=5, b=-6))
