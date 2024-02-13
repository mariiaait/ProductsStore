"""Business logic of project, namely, exception handling(decorators), logs, converting etc."""
import DataManager.json_file_repository as repository
from Configuration.config import PATH_TO_JSON_FILE, PRODUCT_ID


def add(path: str, *args: tuple) -> bool:
    """Business logic of adding data to file.
    path - this is the path to the file with basic data for CRUD.
    args - data which adds to the file by path."""
    data = None
    return repository.add(PATH_TO_JSON_FILE, data)


def get(path: str) -> dict[list[dict]]:
    """Business logic of getting data from file.
       path - this is the path to the file with basic data for CRUD."""
    return repository.get(PATH_TO_JSON_FILE)


def get_by_id(path: str, id: int) -> dict:
    """Business logic of getting data from file by id.
         path - this is the path to the file with basic data for CRUD.
         id - this is id of data."""
    return repository.get_by_id(PATH_TO_JSON_FILE, PRODUCT_ID)


def delete(path: str, id: int) -> bool:
    """Business logic of deleting data from file by id.
         path - this is the path to the file with basic data for CRUD.
         id - this is id of data."""
    return repository.delete(PATH_TO_JSON_FILE, PRODUCT_ID)


def update(path: str, *args: tuple) -> bool:
    """Business logic of updating data in file.
             path - this is the path to the file with basic data for CRUD.
             args - data to update."""
    data = None
    return repository.update(PATH_TO_JSON_FILE, data)


def get_last(path: str) -> dict:
    """Business logic of getting last data from file.
          path - this is the path to the file with basic data for CRUD."""
    return repository.get_last(PATH_TO_JSON_FILE)
