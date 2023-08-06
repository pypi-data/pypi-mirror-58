from .mixconf import MixConf
from pyaml import yaml


class YamlConf(MixConf):
    extension = "yaml"

    def load_from_file(self, filename):
        with open(filename, "r") as f:
            return yaml.load(f, Loader=yaml.FullLoader)
