from logging import Logger
from typing import Optional

from car_inventory_service.src.commands.command_interface import ICommand
from car_inventory_service.src.models.car import CarStatus
from car_inventory_service.src.repositories.car.car_repository import ICarRepository


class GetAllCars(ICommand):
    def __init__(self, repository: ICarRepository, logger: Logger, status: Optional[CarStatus] = None):
        self._repository = repository
        self._logger = logger
        self._status = status

    def execute(self):
        self._repository.query_all(self._status)