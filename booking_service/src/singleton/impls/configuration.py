import os

from booking_service.src.models.config import Config
from booking_service.src.singleton.singleton import SingletonMeta
from booking_service.src.utils.config import load_config


class Configuration(metaclass=SingletonMeta):
    def __init__(self):
        configuration_file_path = os.getenv("BOOKING_CONFIG_PATH", "\configuration.yaml")
        self.settings : Config = load_config(configuration_file_path)
