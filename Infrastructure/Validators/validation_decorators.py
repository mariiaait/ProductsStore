"""Decorators of validation for json_file_service file."""

import logging
import ProductsStore.Configuration.config as configuration

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=configuration.PATH_TO_LOG_FILE)


def validate_existing_file(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except FileNotFoundError as ex:
            write_log(ex)

    return wrapper


def write_log(ex):
    # Log the exception message
    logging.error(f"File not found: {ex}")
