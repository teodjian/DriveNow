from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer,UUID, Enum as SAEnum
from car_inventory_service.src.models.car import Car, CarStatus


Base = declarative_base()

class CarDbModel(Base):
    """
    SQLAlchemy ORM model representing the 'cars' table in PostgreSQL.
    """
    __tablename__ = 'cars' # TODO: change with

    id = Column(UUID, primary_key=True)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    status = Column(SAEnum(CarStatus, name="car_status_enum"), default=CarStatus.AVAILABLE)

    def to_domain(self) -> Car:
        """Helper to convert DB model to Domain Entity"""
        return Car(
            id=self.id,
            model=self.model,
            year=self.year,
            status = self.status)


    @staticmethod
    def from_domain(entity: Car) -> "CarDbModel":
        """Helper to convert Domain Entity to DB model"""
        return CarDbModel(
            id=entity.id,
            model=entity.model,
            year=entity.year,
            status=entity.status
        )
