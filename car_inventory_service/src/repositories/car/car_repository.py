from abc import ABC, abstractmethod
from typing import Optional, List
from car_inventory_service.src.models.car import Car, CarStatus


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
    def update(self, identifier: str, new_status: CarStatus) -> bool:
        """
        update the car status
        :param identifier: car identifier
        :param new_status: the new status of the car to update
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
    def query_all(self, status: Optional[CarStatus] = None) -> Optional[List[Car]]:
        """
        query all cars
        :return: return all the cars
        """