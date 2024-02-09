"""Initializing of test data from test_data.json file to data.json file."""

import json
import ProductsStore.Configuration.config as configuration
import ProductsStore.Infrastructure.Validators.validation_decorators as decorator


@decorator.validate_existing_file
def initialize(from_file_path: str, to_file_path: str) -> None:
    """Initialize basic file with data from another.
    from_file_path - path from file with data.
    to_file_path - path to file in which data should be written."""
    with open(from_file_path) as file:
        data_json = json.load(file)

    with open(to_file_path, 'w') as file:
        json.dump(data_json, file)


initialize(configuration.PATH_TO_TEST_JSON_FILE, configuration.PATH_TO_JSON_FILE)
