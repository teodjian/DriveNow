from typing import Optional

from car_inventory_service.src.models.car import Car, CarStatus
from fastapi import APIRouter

router = APIRouter()


@router.get("/car_inventory/car_by_id/{id}")
async def get_car_by_id(car_id:int):
   pass

@router.put("/car_inventory/update_status")
def update_car(car:Car):
    pass

@router.get("/car_inventory/all_cars")
def get_all_cars(filter_status: Optional[CarStatus] = None):
    pass

@router.post("/car_inventory/car")
def create_car(car: Car):
    pass
