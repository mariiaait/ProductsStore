"""Business logic of project, namely, exception handling(decorators), logs, converting etc."""


def add(path: str, *args: tuple) -> bool:
    """Business logic of adding data to file.
    path - this is the path to the file with basic data for CRUD.
    args - data which adds to the file by path."""
    pass


def get(path: str) -> dict[list[dict]]:
    """Business logic of getting data from file.
       path - this is the path to the file with basic data for CRUD."""
    pass


def get_by_id(path: str, id: int) -> dict:
    """Business logic of getting data from file by id.
         path - this is the path to the file with basic data for CRUD.
         id - this is id of data."""
    pass


def delete(path: str, id: int) -> bool:
    """Business logic of deleting data from file by id.
         path - this is the path to the file with basic data for CRUD.
         id - this is id of data."""
    pass


def update(path: str, *args: tuple) -> bool:
    """Business logic of updating data in file.
             path - this is the path to the file with basic data for CRUD.
             args - data to update."""
    pass


def get_last() -> dict:
    """Business logic of getting last data from file.
          path - this is the path to the file with basic data for CRUD."""
    pass
