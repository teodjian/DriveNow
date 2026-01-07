import logging
import requests
from pydantic import UUID4

from booking_service.src.models.config import CarInventoryApiConfig


class InventoryConnector:
    def __init__(self, inventory_service_config: CarInventoryApiConfig, logger: logging.Logger):
        self.inventory_service_config = inventory_service_config
        self.logger = logger

    def is_car_available(self, car_id: UUID4) -> bool:
        try:
            url = f"{self.inventory_service_config.url}{car_id}"
            response = requests.get(url)
            if response.status_code == 404:
                self.logger.warning(f"Car {car_id} is not found")
                return False
            if response.status_code != 200:
                self.logger.warning(f"Inventory Service returned error: {response.status_code}")
                return False
            car_data = response.json()
            return car_data.get("status") == "available"
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to connect to Inventory Service: {e}")
            return False

    def change_car_status(self, car_id: UUID4, status) -> None:
        pass