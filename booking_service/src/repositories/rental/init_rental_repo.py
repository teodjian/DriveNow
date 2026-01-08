import logging

from booking_service.src.models.config import Config
from booking_service.src.repositories.rental.impls.postgresql import PostgresRentalRepository


def create_rental_repo(config: Config, logger: logging.Logger):
    rental_db = config.database
    return PostgresRentalRepository(str(rental_db.database_url), logger)
