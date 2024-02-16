"""Business logic of project, namely, exception handling(decorators), logs, converting etc."""
import DataManager.json_file_repository as repository
from Infrastructure.Converters.to_dict import to_dict
from Infrastructure.Validators.validation_decorators import check_parameters_types, handle_crud_exceptions

@handle_crud_exceptions("Add data to json file")
@check_parameters_types
def add(path: str, id: int, name: str) -> dict:
    """Business logic of adding data to file.
    path - this is the path to the file with basic data for CRUD.
    args - data which adds to the file by path."""
    data = to_dict(id, name)
    return repository.add(path, data)

@handle_crud_exceptions("Get data from json file")
@check_parameters_types
def get(path: str) -> dict:
    """Business logic of getting data from file.
       path - this is the path to the file with basic data for CRUD."""
    return repository.get(path)

@handle_crud_exceptions("Get data by_id from json file")
@check_parameters_types
def get_by_id(path: str, id: int) -> dict:
    """Business logic of getting data from file by id.
         path - this is the path to the file with basic data for CRUD.
         id - this is id of data."""
    return repository.get_by_id(path, id)

@handle_crud_exceptions("Delete data from json file")
@check_parameters_types
def delete(path: str, id: int) -> dict:
    """Business logic of deleting data from file by id.
         path - this is the path to the file with basic data for CRUD.
         id - this is id of data."""
    return repository.delete(path, id)

@handle_crud_exceptions("Update data in json file")
@check_parameters_types
def update(path: str, id: int, name: str) -> dict:
    """Business logic of updating data in file.
             path - this is the path to the file with basic data for CRUD.
             args - data to update."""
    data = to_dict(id, name)
    return repository.update(path, data)

@handle_crud_exceptions("Get last record from json file")
@check_parameters_types
def get_last(path: str) -> dict:
    """Business logic of getting last data from file.
          path - this is the path to the file with basic data for CRUD."""
    return repository.get_last(path)
