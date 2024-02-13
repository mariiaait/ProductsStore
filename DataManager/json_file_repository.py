"""CRUD operations. Executing of request only. If request throw an exception,
the functions in the 'json_file_service' will handle it."""
import json
from Configuration.config import PRODUCT_ID, PRODUCTS, INDENT, PRODUCT_NAME


def add(path: str, data: dict) -> None:
    """Represents the logic of adding data to file.
     path - this is the path to the file with basic data for CRUD.
     data - data to add."""
    all_data = get(path)
    if not is_exists(data, all_data):
        all_data[PRODUCTS].append(data)
        write(path, all_data)


def is_exists(data: dict, all_data: dict) -> bool:
    return any(map(lambda item: item[PRODUCT_ID] == data[PRODUCT_ID], all_data[PRODUCTS]))


def write(path, data):
    with open(path, 'w') as file:
        json.dump(data, file, indent=INDENT)


def get(path: str) -> dict[list[dict]]:
    """Represents the logic of getting data from file.
     path - this is the path to the file with basic data for CRUD."""
    with open(path) as file:
        return json.load(file)


def get_by_id(path: str, id: int) -> dict | None:
    """Represents the logic of getting data from file by id.
     path - this is the path to the file with basic data for CRUD.
     id - this is id of data."""
    all_data = get(path)
    for item in all_data[PRODUCTS]:
        if item[PRODUCT_ID] == id:
            return item
    return None


def delete(path: str, id: int) -> None:
    """Represents the logic of deleting data from file by id.
         path - this is the path to the file with basic data for CRUD.
         id - this is id of data."""
    all_data = get(path)
    for item in all_data[PRODUCTS]:
        if item[PRODUCT_ID] == id:
            all_data[PRODUCTS].remove(item)
            write(path, all_data)
            return


def update(path: str, data: dict) -> None:
    """Represents the logic of updating data to file.
         path - this is the path to the file with basic data for CRUD.
         data - data to update."""
    all_data = get(path)
    if not is_exists(data, all_data):
        all_data[PRODUCTS].append(data)
    else:
        all_data[PRODUCTS] = list(map(lambda item: data if item[PRODUCT_ID] == data[PRODUCT_ID]
        else item, all_data[PRODUCTS]))
    write(path, all_data)


def get_last(path: str) -> dict:
    """Represents the logic of getting last data from file.
         path - this is the path to the file with basic data for CRUD."""
    all_data = get(path)
    return all_data[PRODUCTS][-1]
