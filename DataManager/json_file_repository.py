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
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            if 'products' in data and isinstance(data['products'], list):
                for product in data['products']:
                    if 'id' in product and product['id'] == id:
                        return product
                print(f"No data found with id {id}.")
                return None
            else:
                print("Invalid JSON structure or missing 'products' list.")
                return None
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON file: {path}")
        return None


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


def get_last(path: str) -> dict:
    """Represents the logic of getting last data from file.
         path - this is the path to the file with basic data for CRUD."""
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            if 'products' in data and isinstance(data['products'], list) and len(data['products']) > 0:
                last_item = data['products'][-1]
                return last_item
            else:
                print("Invalid JSON structure or empty 'products' list.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON file: {file_path}")
