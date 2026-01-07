from abc import ABC, abstractmethod
from typing import Generic

from car_inventory_service.src.models.car import Car


class ICommand(ABC):
    @abstractmethod
    def execute(self) :
        """
        Execute the command
        :return:
        """
