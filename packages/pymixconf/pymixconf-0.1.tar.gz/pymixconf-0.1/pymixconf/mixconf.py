import os
from copy import deepcopy
from abc import abstractmethod


class MixConf:
    extension = "NOTSET"

    def __init__(self, config_directory="config", environment_key="CONFIG_ENV"):
        self.environment_key = environment_key
        self.config_directory = config_directory

    @abstractmethod
    def load_from_file(self, filename: str) -> dict:
        pass

    def merge_configs(self, config_a: dict, config_b: dict) -> dict:
        if not isinstance(config_b, dict):
            return config_b

        merged = {}
        keys = list(config_a.keys()) + list(config_b.keys())
        for key in keys:
            if key in config_a and key in config_b:
                merged[key] = self.merge_configs(config_a[key], config_b[key])
            else:
                merged[key] = config_a.get(key, config_b.get(key))
        return merged

    def load_config(self) -> dict:
        conf = {}
        for filename in self.precidence:
            try:
                conf = self.merge_configs(conf, self.load_from_file(filename))
            except Exception as ex:
                print("Error loading config .{}".format(ex)) 
        return conf

    @property
    def precidence(self) -> list:
        return [
            os.path.join(self.config_directory, "config.{}".format(self.extension)),
            os.path.join(
                self.config_directory, "{}.config.{}".format(self.environment, self.extension)
            ),
            os.path.join(
                self.config_directory,
                "{}.secret.{}".format(self.environment, self.extension),
            ),
        ]

    @property
    def environment(self):
        return os.environ.get(self.environment_key, "dev")
