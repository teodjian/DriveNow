from sqlalchemy import Column, UUID, ForeignKey, String, DateTime
from sqlalchemy.orm import declarative_base

from booking_service.src.models.rental import Rental
from booking_service.src.singleton.impls.configuration import Configuration

Base = declarative_base()
class RentalDbModel(Base):
    __tablename__ = Configuration().settings.database.table_name
    id = Column(UUID, primary_key=True)
    car_id = Column(UUID, nullable=False)
    customer_name = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)

    def to_domain(self) -> Rental:
        """Helper to convert DB model to Domain Entity"""
        return Rental(
            id=self.id,
            car_id=self.car_id,
            customer_name=self.customer_name,
            start_date=self.start_date,
            end_date=self.end_date)


    @staticmethod
    def from_domain(entity: Rental) -> "RentalDbModel":
        """Helper to convert Domain Entity to DB model"""
        return RentalDbModel(
            id=entity.id,
            car_id=entity.car_id,
            customer_name=entity.customer_name,
            start_date=entity.start_date,
            end_date=entity.end_date
        )
