import constants as c
import json


SETTINGS = c.SETTINGS_BODY.copy()


def save_as_json(filepath):
    try:
        if filepath.endswith('.json'):
            with open(filepath, 'a') as outfile:
                json.dump(SETTINGS, outfile, indent=4)
        else:
            filepath = f'{filepath}.json'
            with open(filepath, 'a') as outfile:
                json.dump(SETTINGS, outfile, indent=4)
    except Exception:
        print(c.JSON_SAVE_ERROR)


def load_json(filepath):
    global SETTINGS
    try:
        with open(filepath, 'r') as inputfile:
            SETTINGS = json.load(inputfile)
            return True
    except Exception:
        print(c.JSON_LOAD_ERROR)
