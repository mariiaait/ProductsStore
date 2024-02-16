"""Decorators of validation for json_file_service file."""
from functools import wraps
from typing import get_type_hints, Callable
import logging
from Configuration.config import PATH_TO_LOG_FILE


def check_parameters_types(func) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        type_hints = get_type_hints(func)
        args_lst = list(args)
        args_lst.extend(kwargs.values())
        pairs = list(zip(type_hints, args_lst))
        for name, value in pairs:
            type_hint = type_hints[name]
            if not isinstance(value, type_hint):
                raise TypeError(f'Expected {type_hint}. Got {type(value)}')
        return func(*args, **kwargs)

    return wrapper


logging.basicConfig(filename=PATH_TO_LOG_FILE, format='%(asctime)s - %(levelname)s - %(message)s')


def handle_crud_exceptions(log_mes: str) -> Callable:
    def check_exception(func) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logging.info(log_mes)
                response = func(*args, **kwargs)
                return {"is_success": True, "response": response, "errors": None}
            except Exception as ex:
                logging.error(ex)
                return {"is_success": False, "response": None, "errors": str(ex)}

        return wrapper

    return check_exception
