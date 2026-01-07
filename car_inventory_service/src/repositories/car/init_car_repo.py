from logging import Logger
from car_inventory_service.src.models.config import Config
from car_inventory_service.src.repositories.car.impls.postgresql import PostgresCarRepository


def create_car_repo(config: Config, logger: Logger):
    db = config.database
    return PostgresCarRepository(str(db.database_url), logger)
