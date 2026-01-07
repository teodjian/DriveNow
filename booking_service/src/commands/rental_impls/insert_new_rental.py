from logging import Logger

from booking_service.src.commands.command_interface import ICommand
from booking_service.src.models.rental import Rental
from booking_service.src.repositories.rental.rental_repository import IRentalRepository
from booking_service.src.utils.metrics import add_rental


class InsertNewRental(ICommand):
    def __init__(self, repository: IRentalRepository, logger: Logger, rental: Rental):
        self._repository = repository
        self._logger = logger
        self._rental = rental

    def execute(self):
        add_rental()
        self._repository.insert_rental(self._rental)
