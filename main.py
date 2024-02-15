import json

from Infrastructure.Initializer import default_file_initializer as initializer
from Configuration.config import PATH_TO_JSON_FILE, DEFAULT_FILE_DATA, PATH_TO_TEST_JSON_FILE
import BusinessLogic.json_file_service as service
import os

"""Main file for project run."""
def input_data(*args):
    data =[]
    for arg in args:
        temp = input(f"Input {arg}: ")
        if arg=='id':
            temp=int(temp)
        data.append(temp)
    return data

def main() -> None:
    """Function with project's run logic.
    path - this is the path to the file with basic data for CRUD."""
    create_or_default(PATH_TO_JSON_FILE)
    initializer.initialize(PATH_TO_TEST_JSON_FILE, PATH_TO_JSON_FILE)
    print(service.get_last(PATH_TO_JSON_FILE))

    while True:
        command = input("Input a command (add, update, delete, get, get_by_id, get_last, exit): ")

        if command=='add':
            data = input_data('id', 'name')
            print(service.add(PATH_TO_JSON_FILE, *data))
        elif command == 'update':
            data = input_data('id', 'name')
            print(service.update(PATH_TO_JSON_FILE, *data))
        elif command == 'delete':
            data = input_data('id')
            print(service.delete(PATH_TO_JSON_FILE, *data))
        elif command == 'get':
            print(service.get(PATH_TO_JSON_FILE))
        elif command == 'get_by_id':
            data = input_data('id')
            print(service.get_by_id(PATH_TO_JSON_FILE, *data))
        elif command == 'get_last':
            print(service.get_last(PATH_TO_JSON_FILE))
        elif command == 'exit':
            break
        else:
            print ('Wrong command. Try again!')


def create_or_default(path):
    if (os.path.exists(path) and os.path.getsize(path)==0) or (not os.path.exists(path)):
        with open(path, 'w') as file:
            json.dump(DEFAULT_FILE_DATA, file)



if __name__ == "__main__":
    """Run of the project."""
    main()




