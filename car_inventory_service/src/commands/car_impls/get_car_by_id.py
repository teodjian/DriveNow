from logging import Logger
from pydantic import UUID4
from car_inventory_service.src.commands.command_interface import ICommand
from car_inventory_service.src.repositories.car.car_repository import ICarRepository

class GetCarById(ICommand):
    def __init__(self, repository: ICarRepository, logger: Logger, car_id: UUID4):
        self._repository = repository
        self._logger = logger
        self._car_id = car_id

    def execute(self):
        return self._repository.query_one(str(self._car_id))