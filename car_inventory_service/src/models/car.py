import enum
from typing import Optional

from pydantic import BaseModel, UUID4


class CarStatus(enum.Enum):
    AVAILABLE = "available"
    IN_USE = "in_use"
    MAINTENANCE = "maintenance"


class Car(BaseModel):
    id: UUID4
    model: str
    year: int
    status: CarStatus

class CarToUpdate(BaseModel):
    id: UUID4
    model: Optional[str] = None
    year: Optional[int] = None
    status: CarStatus