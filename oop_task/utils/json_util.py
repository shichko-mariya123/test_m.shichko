import json
import os


def load_data_from_json(file_name):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(project_root, file_name)
    with open(file_path, "r") as file:
        return json.load(file)
