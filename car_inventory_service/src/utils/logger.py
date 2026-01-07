import logging
import logging.config

from car_inventory_service.src.models.config import LoggerConfig
from car_inventory_service.src.singleton.impls.configuration import Configuration


def config_logger() -> logging.Logger:
    logger_config: LoggerConfig = Configuration().settings.logging
    logging.config.dictConfig(logger_config.logging_dict)
    logger = logging.getLogger(logger_config.logger_name)
    return logger
