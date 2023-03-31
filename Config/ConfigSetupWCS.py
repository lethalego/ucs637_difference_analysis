import json


def get_value_from_json(json_file, key, sub_key):
    try:
        with open(json_file) as f:
            data = json.load(f)
            return data[key][sub_key]
    except Exception as e:
        print("Error: ", e)


class ConfigSetupWCS:

    path = "../resources/mapConfigWCS.json"

    def __init__(self, path=path):
        print("Calling the __init__() constructor!\n")

        self.time_range = get_value_from_json(path, "map", "time_range")
        self.coords_wgs84 = get_value_from_json(path, "map", "coords_wgs84")
        self.coords_wgs84_WCS = get_value_from_json(path, "map", "coords_wgs84")
        self.cloud_coverage = get_value_from_json(path, "map", "cloud_coverage")
        self.data_collection = get_value_from_json(path, "map", "data_collection")
        self.layer = get_value_from_json(path, "map", "layer")
        self.resX = get_value_from_json(path, "map", "resX")
        self.resY = get_value_from_json(path, "map", "resY")
        self.data_folder = get_value_from_json(path, "map", "data_folder")



