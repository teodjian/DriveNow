from abc import ABC, abstractmethod
from typing import Optional, List

from car_inventory_service.src.models.car import Car


class ICarRepository(ABC):
    """
    Interface for car repositories, definning the basic CRUD operations for car data
    """
    @abstractmethod
    def insert(self, entity: Car) -> None:
        """
        insert a new car
        :param entity: information about the car
        :return:
        """

    @abstractmethod
    def update(self, entity: Car) -> bool:
        """
        update the car information
        :param entity:
        :return:
        """

    @abstractmethod
    def query_one(self, identifier: str) -> Optional[Car]:
        """
        query a car based on its id
        :param identifier:
        :return:
        """

    @abstractmethod
    def query_all(self) -> Optional[List[Car]]:
        """
        query all cars
        :return: return all the cars
        """