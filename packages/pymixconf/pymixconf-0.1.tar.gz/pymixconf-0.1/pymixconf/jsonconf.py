import json
from .mixconf import MixConf


class JSONConf(MixConf):
    extension = "json"

    def load_from_file(self, filename):
        with open(filename, "r") as f:
            return json.load(f)
