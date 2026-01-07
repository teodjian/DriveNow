from logging import Logger

from car_inventory_service.src.commands.command_interface import ICommand
from car_inventory_service.src.models.car import Car
from car_inventory_service.src.repositories.car.car_repository import ICarRepository


class InsertCar(ICommand):
    def __init__(self, repository: ICarRepository, logger: Logger, car: Car):
        self._repository = repository
        self._logger = logger
        self._car = car

    def execute(self):
        self._repository.insert(self._car)
