import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from booking_service.src.models.rental import Rental
from booking_service.src.models.rental_postgres_model import Base, RentalDbModel
from booking_service.src.repositories.rental.rental_repository import IRentalRepository, EntityAlreadyExistsError, \
    EntityNotExistsError


class PostgresRentalRepository(IRentalRepository):
    def __init__(self, connection_string: str, logger: logging.Logger):
        """
        Initialize with a PostgreSQL connection string.
        """
        self.logger = logger
        self.engine = create_engine(connection_string)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        Base.metadata.create_all(bind=self.engine)

    def insert_rental(self, entity: Rental) -> None:
        session: Session = self.SessionLocal()
        try:
            db_rental = RentalDbModel.from_domain(entity)
            session.add(db_rental)
            session.commit()
            self.logger.debug(f"New rental {entity.id}, for car {entity.car_id} is successfully added to database")

        except Exception as e:
            self.logger.error(f"Rental {entity.id}, for car {entity.car_id} is not successfully added to database {e}")
            session.rollback()
            raise EntityAlreadyExistsError(f"Rental already exists for car {entity.car_id}")
        finally:
            session.close()

    def end_rental(self, entity: Rental) -> None:
        session: Session = self.SessionLocal()
        try:
            db_rental = session.get(RentalDbModel, entity.id)
            if not db_rental:
                self.logger.warning(f"rental {entity.id} is not found in the database")
                raise EntityNotExistsError(f"rental with {entity.id} not found")
            db_rental.end_date = entity.end_date
            session.commit()
            self.logger.debug(f"Rental {entity.id} is successfully ended")
        except Exception as e:
            session.rollback()
            self.logger.error(f"failed to end the rental {entity.id} of car {entity.car_id} {e}")
        finally:
            session.close()
