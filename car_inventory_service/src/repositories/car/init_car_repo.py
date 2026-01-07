from car_inventory_service.src.models.config import Config
from car_inventory_service.src.repositories.car.impls.postgresql import PostgresCarRepository


def create_car_repo(config: Config, logger):
    db = config.database
    return PostgresCarRepository(str(db.connection_string),logger)

