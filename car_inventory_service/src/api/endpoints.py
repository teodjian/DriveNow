import time
from typing import Optional

from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from pydantic import UUID4
from car_inventory_service.src.commands.car_impls.get_all_cars import GetAllCars
from car_inventory_service.src.commands.car_impls.get_car_by_id import GetCarById
from car_inventory_service.src.commands.car_impls.insert_car import InsertCar
from car_inventory_service.src.commands.car_impls.update_car import UpdateCar
from car_inventory_service.src.models.car import Car, CarStatus, CarToUpdate
from fastapi import APIRouter, Response, HTTPException
from car_inventory_service.src.repositories.car.init_car_repo import create_car_repo
from car_inventory_service.src.singleton.impls.configuration import Configuration
from car_inventory_service.src.singleton.impls.logger import Logger
from car_inventory_service.src.utils.metrics import observe_latency

router = APIRouter()
service_logger = Logger().logger
configuration = Configuration().settings
repository = create_car_repo(config=configuration, logger=service_logger)


@router.get("/metrics")
async def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)


@router.get("/car_inventory/car_by_id/{identifier}")
async def get_car_by_id(identifier: UUID4):
    command = GetCarById(repository=repository, logger=service_logger, car_id=identifier)
    result = command.execute()
    if result is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return result


@router.put("/car_inventory/update_status")
async def update_car(car: CarToUpdate):
    command = UpdateCar(repository=repository, logger=service_logger, car=car)
    command.execute()


@router.get("/car_inventory/all_cars")
async def get_all_cars(filter_status: Optional[CarStatus] = None):
    command = GetAllCars(repository=repository, logger=service_logger, status=filter_status)
    start_time = time.time()
    result =command.execute()
    duration = time.time() - start_time
    observe_latency(
        method="GET",
        endpoint="/car_inventory/all_cars",
        duration=duration
    )
    return result


@router.post("/car_inventory/car")
async def create_car(car: Car):
    command = InsertCar(repository=repository, logger=service_logger, car=car)
    start_time = time.time()
    command.execute()
    duration = time.time() - start_time
    observe_latency(
        method="POST",
        endpoint="/car_inventory/car",
        duration=duration
    )
