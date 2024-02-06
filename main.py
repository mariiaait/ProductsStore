from Configuration.config import PATH_TO_JSON_FILE
import json

"""Main file (run project)"""


def to_dict(id, name):
    pass


def main(path):
    pass


if __name__ == "__main__":
    # main(PATH_TO_JSON_FILE)
    # with open(PATH_TO_JSON_FILE, "w") as file:
    #     json.dump({"id": 2, "name": "carrot"}, file)

    with open(PATH_TO_JSON_FILE, "r") as file:
        data = json.load(file)

    print(data)
    data["products"].append({"id": 3, "name": "potato"})

    with open(PATH_TO_JSON_FILE, "w") as file:
        json.dump(data, file, indent=3)