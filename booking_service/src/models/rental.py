import datetime
from typing import Optional

from pydantic import BaseModel, UUID4


class Rental(BaseModel):
    id: UUID4
    car_id: UUID4
    customer_name: str
    start_date: datetime.datetime
    end_date: Optional[datetime.datetime] = None