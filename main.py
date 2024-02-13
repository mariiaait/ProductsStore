import json

from Infrastructure.Initializer import default_file_initializer as initializer
from Configuration.config import PATH_TO_JSON_FILE, DEFAULT_FILE_DATA, PATH_TO_TEST_JSON_FILE
import DataManager.json_file_repository as repository
import os

"""Main file for project run."""


def main() -> None:
    """Function with project's run logic.
    path - this is the path to the file with basic data for CRUD."""
    create_or_default(PATH_TO_JSON_FILE)
    initializer.initialize(PATH_TO_TEST_JSON_FILE, PATH_TO_JSON_FILE)
    print (repository.get(PATH_TO_JSON_FILE))
    print (repository.get_last(PATH_TO_JSON_FILE))
    print (repository.get_by_id(PATH_TO_JSON_FILE, 4))

def create_or_default(path):
    if (os.path.exists(path) and os.path.getsize(path)==0) or (not os.path.exists(path)):
        with open(path, 'w') as file:
            json.dump(DEFAULT_FILE_DATA, file)



if __name__ == "__main__":
    """Run of the project."""
    main()




