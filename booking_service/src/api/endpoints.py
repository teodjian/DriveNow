from fastapi import APIRouter, HTTPException, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from booking_service.src.commands.rental_impls.end_rental import EndRental
from booking_service.src.commands.rental_impls.insert_new_rental import InsertNewRental
from booking_service.src.models.config import CarInventoryApiConfig
from booking_service.src.models.rental import Rental
from booking_service.src.repositories.rental.init_rental_repo import create_rental_repo
from booking_service.src.singleton.impls.configuration import Configuration
from booking_service.src.singleton.impls.logger import Logger
from booking_service.src.utils.inventory_connector import InventoryConnector

router = APIRouter()
booking_logger = Logger().logger
booking_configuration = Configuration().settings
rental_repository = create_rental_repo(booking_configuration, booking_logger)


@router.get("/metrics")
async def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)


@router.post("/booking/start_rental")
async def start_rental(rental: Rental):
    inventory_service_configuration: CarInventoryApiConfig = booking_configuration.car_inventory_api
    connector = InventoryConnector(inventory_service_configuration, booking_logger)
    if connector.is_car_available(rental.car_id):
        if connector.change_car_status(rental.car_id, "in_use"):
            command = InsertNewRental(rental_repository, booking_logger, rental)
            command.execute()
        else:
            raise HTTPException(status_code=400, detail="failed update car so no rental booked.")
    else:
        raise HTTPException(status_code=400, detail="Car is not available or does not exist.")


@router.put("/booking/end_rental")
async def end_rental(rental: Rental):
    inventory_service_configuration: CarInventoryApiConfig = booking_configuration.car_inventory_api
    connector = InventoryConnector(inventory_service_configuration, booking_logger)
    if connector.change_car_status(rental.car_id, "available"):
        command = EndRental(rental_repository, booking_logger, rental)
        command.execute()
    else:
        raise HTTPException(status_code=400, detail="failed to end car rental.")
