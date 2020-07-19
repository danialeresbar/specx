import json


CONFIG = dict()


def save_as_json(filepath):
    if filepath.endswith(".json"):
        with open(filepath, 'a') as outfile:
            json.dump(CONFIG, outfile, indent=4)
    else:
        filepath = "{}{}".format(filepath, ".json")
        with open(filepath, 'a') as outfile:
            json.dump(CONFIG, outfile, indent=4)


def load_json(filepath):
    global CONFIG
    CONFIG = json.load(open(filepath, 'r'))
