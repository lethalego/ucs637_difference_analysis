import json


def get_value_from_json(json_file, key, sub_key):
    try:
        with open(json_file) as f:
            data = json.load(f)
            return data[key][sub_key]
    except Exception as e:
        print("Error: ", e)


print(get_value_from_json("mapConfig.json", "db", "host"))  # prints localhost
