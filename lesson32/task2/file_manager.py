import json


def write_to_file(data: dict) -> None:
    with open('comments.json', 'w') as outfile:
        json.dump(data, outfile)
