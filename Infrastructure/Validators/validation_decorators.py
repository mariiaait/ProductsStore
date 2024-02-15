"""Decorators of validation for json_file_service file."""
from functools import wraps
from typing import get_type_hints, Callable


def check_parameters_types(func)->Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        type_hints = get_type_hints(func)
        args_lst = list(args)
        args_lst.extend(kwargs.values())
        pairs = list(zip(type_hints, args_lst))
        for name, value in pairs:
            type_hint = type_hints[name]
            if not isinstance(value, type_hint):
                raise TypeError (f'Expected {type_hint}. Got {type(value)}')
        return func(*args, **kwargs)

    return wrapper
