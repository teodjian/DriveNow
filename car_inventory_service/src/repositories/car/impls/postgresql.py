import logging
from typing import Optional, List
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session
from car_inventory_service.src.models.car import Car, CarStatus
from car_inventory_service.src.models.car_postgres_model import Base, CarDbModel
from car_inventory_service.src.repositories.car.car_repository import ICarRepository



class PostgresCarRepository(ICarRepository):
    def __init__(self, connection_string: str, logger: logging.Logger):
        """
        Initialize with a PostgreSQL connection string.
        """
        self.logger = logger
        self.engine = create_engine(connection_string)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        Base.metadata.create_all(bind=self.engine)

    def insert(self, entity: Car) -> bool:
        session: Session = self.SessionLocal()
        try:
            db_car = CarDbModel.from_domain(entity)
            session.add(db_car)
            session.commit()
            self.logger.debug(f"car {entity.id} is successfully added to database")
            return True
        except Exception as e:
            self.logger.error(f"car {entity.id} is not successfully added to database {e}")
            session.rollback()
            return False
        finally:
            session.close()

    def update(self, identifier: str, new_status: CarStatus) -> bool:
        session: Session = self.SessionLocal()
        try:
            db_car = session.get(CarDbModel, identifier)
            if not db_car:
                self.logger.warning(f"car {identifier} is not found in database")
                return False
            db_car.model = new_status
            session.commit()
            self.logger.debug(f"car {identifier} is successfully updated in database")
            return True
        except Exception as e:
            session.rollback()
            self.logger.error(f"car {identifier} is not successfully updated in database {e}")
            return False
        finally:
            session.close()

    def query_one(self, identifier: str) -> Optional[Car]:
        session: Session = self.SessionLocal()
        try:
            db_car = session.get(CarDbModel, identifier)
            if db_car:
                self.logger.debug(f"car {identifier} is successfully found in database")
                return db_car.to_domain()

            self.logger.warning(f"car {identifier} is not found in database")
            return None
        except Exception as e:
            self.logger.error(f"failed to query car {identifier}: {e}")
        finally:
            session.close()

    def query_all(self, status: Optional[CarStatus] = None) -> Optional[List[Car]]:
        session: Session = self.SessionLocal()
        try:
            cars = select(CarDbModel)
            if status is not None:
                cars = cars.where(CarDbModel.status == status)
            result = session.execute(cars).scalars().all()
            self.logger.debug(f"return all the cars found in database with the filter")
            return [car.to_domain() for car in result]
        finally:
            session.close()