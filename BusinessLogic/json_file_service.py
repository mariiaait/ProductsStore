"""Business logic of project, namely, exception handling(decorators), logs, converting etc."""
import DataManager.json_file_repository as repository
from Infrastructure.Converters.to_dict import  to_dict

def add(path: str, *args) -> dict:
    """Business logic of adding data to file.
    path - this is the path to the file with basic data for CRUD.
    args - data which adds to the file by path."""
    data = to_dict(args)
    return repository.add(path, data)


def get(path: str) -> dict:
    """Business logic of getting data from file.
       path - this is the path to the file with basic data for CRUD."""
    return repository.get(path)


def get_by_id(path: str, id: int) -> dict:
    """Business logic of getting data from file by id.
         path - this is the path to the file with basic data for CRUD.
         id - this is id of data."""
    return repository.get_by_id(path, id)


def delete(path: str, id: int) -> dict:
    """Business logic of deleting data from file by id.
         path - this is the path to the file with basic data for CRUD.
         id - this is id of data."""
    return repository.delete(path, id)


def update(path: str, *args: tuple) -> dict:
    """Business logic of updating data in file.
             path - this is the path to the file with basic data for CRUD.
             args - data to update."""
    data = to_dict(args)
    return repository.update(path, data)


def get_last(path: str) -> dict:
    """Business logic of getting last data from file.
          path - this is the path to the file with basic data for CRUD."""
    return repository.get_last(path)
