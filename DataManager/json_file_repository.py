"""CRUD operations. Executing of request only. If request throw an exception,
the functions in the 'json_file_service' will handle it."""
import json
from Configuration.config import PRODUCT_ID, PRODUCTS, INDENT
def add(path: str, data: dict) -> None:
    """Represents the logic of adding data to file.
     path - this is the path to the file with basic data for CRUD.
     data - data to add."""
    all_data = get(path)
    if not is_exists(all_data, data):
        all_data[PRODUCTS].append(data)
        write(path, all_data)

def is_exists (data, all_data):
    return any(map(lambda item: item[PRODUCT_ID]==data[PRODUCT_ID], all_data))

def write(path, data):
    with open(path, 'w') as file:
        json.dump(data, file, indent=INDENT)


def get(path: str) -> dict[list[dict]]:
    """Represents the logic of getting data from file.
     path - this is the path to the file with basic data for CRUD."""
    with open(path) as file:
        return json.load(file)


def get_by_id(path: str, id: int) -> dict:
    """Represents the logic of getting data from file by id.
     path - this is the path to the file with basic data for CRUD.
     id - this is id of data."""
    pass


def delete(path: str, id: int) -> None:
    """Represents the logic of deleting data from file by id.
         path - this is the path to the file with basic data for CRUD.
         id - this is id of data."""
    pass


def update(path: str, data: dict) -> None:
    """Represents the logic of updating data to file.
         path - this is the path to the file with basic data for CRUD.
         data - data to update."""
    pass


def get_last() -> dict:
    """Represents the logic of getting last data from file.
         path - this is the path to the file with basic data for CRUD."""
    pass
