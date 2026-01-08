from abc import ABC, abstractmethod

from booking_service.src.models.rental import Rental

class EntityAlreadyExistsError(Exception):
    """
    Raised when a car with similar identifier already exists
    """

class EntityNotExistsError(Exception):
    """
    Raised when a car with provided identifier does not exist.
    """

class IRentalRepository(ABC):
    """
    Interface for rental repositories, definning the basic CRUD operations for rental data
    """
    @abstractmethod
    def insert_rental(self, entity: Rental) -> None:
        """
        insert a new rental
        :param entity: information about the rental
        :return:
        """

    @abstractmethod
    def end_rental(self, entity: Rental) -> None:
        """
        end rental
        :param entity: information about the car
        :return:
        """