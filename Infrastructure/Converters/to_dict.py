"""File which responsible for converting passed data to dict type."""

from Configuration.config import PRODUCT_ID, PRODUCT_NAME


def to_dict(*args: tuple) -> dict:
    """Function which converts passed data to dictionary.
    *args - data to convert."""
    if len(args) == 2:
        id, name = args
        return {PRODUCT_ID: id, PRODUCT_NAME: name}
    else:
        raise ValueError("There are not two arguments")
