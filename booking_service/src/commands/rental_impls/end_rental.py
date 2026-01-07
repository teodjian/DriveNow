from booking_service.src.commands.command_interface import ICommand
from booking_service.src.models.rental import Rental
from booking_service.src.repositories.rental.rental_repository import IRentalRepository
from booking_service.src.singleton.impls.logger import Logger
from booking_service.src.utils.metrics import remove_rental


class EndRental(ICommand):
    def __init__(self, repository: IRentalRepository, logger: Logger, rental: Rental):
        self._repository = repository
        self._logger = logger
        self._rental = rental

    def execute(self):
        remove_rental()
        self._repository.end_rental(self._rental)