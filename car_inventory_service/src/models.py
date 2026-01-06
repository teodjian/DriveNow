import enum
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
