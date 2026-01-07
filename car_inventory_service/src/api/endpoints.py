from typing import Optional
from pydantic import UUID4
from car_inventory_service.src.commands.car_impls.get_all_cars import GetAllCars
from car_inventory_service.src.commands.car_impls.get_car_by_id import GetCarById
from car_inventory_service.src.commands.car_impls.insert_car import InsertCar
from car_inventory_service.src.commands.car_impls.update_car import UpdateCar
from car_inventory_service.src.models.car import Car, CarStatus
from fastapi import APIRouter
from car_inventory_service.src.repositories.car.init_car_repo import create_car_repo
from car_inventory_service.src.singleton.impls.configuration import Configuration
from car_inventory_service.src.singleton.impls.logger import Logger

router = APIRouter()
service_logger = Logger().logger
configuration = Configuration().settings
repository = create_car_repo(config=configuration, logger=service_logger)


@router.get("/car_inventory/car_by_id/{identifier}")
def get_car_by_id(identifier: UUID4):
    command = GetCarById(repository=repository, logger=service_logger, car_id=identifier)
    command.execute()


@router.put("/car_inventory/update_status")
def update_car(car: Car):
    command = UpdateCar(repository=repository, logger=service_logger, car=car)
    command.execute()


@router.get("/car_inventory/all_cars")
def get_all_cars(filter_status: Optional[CarStatus] = None):
    command = GetAllCars(repository=repository, logger=service_logger, status=filter_status)
    command.execute()


@router.post("/car_inventory/car")
def create_car(car: Car):
    command = InsertCar(repository=repository, logger=service_logger, car=car)
    command.execute()
