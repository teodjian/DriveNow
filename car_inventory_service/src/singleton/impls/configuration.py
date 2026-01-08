import os

from car_inventory_service.src.models.config import Config
from car_inventory_service.src.singleton.singleton import SingletonMeta
from car_inventory_service.src.utils.config import load_config


class Configuration(metaclass=SingletonMeta):
    def __init__(self):
        configuration_file_path = os.getenv("CONFIG_PATH", "C:\\Users\\Lenovo\\PycharmProjects\\DriveNow\\car_inventory_service\\configuration.yaml")
        self.settings : Config = load_config(configuration_file_path)
