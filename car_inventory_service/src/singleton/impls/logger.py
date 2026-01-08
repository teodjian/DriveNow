from car_inventory_service.src.singleton.singleton import SingletonMeta
from car_inventory_service.src.utils.logger import config_logger


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.logger : Logger = config_logger()