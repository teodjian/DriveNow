from typing import Any
from pydantic import BaseModel, PostgresDsn, ConfigDict


class LoggerConfig(BaseModel):
    logger_name: str
    logging_dict: dict[str, Any]
    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
    )

class PostgresqlConfig(BaseModel):
    database_url: PostgresDsn
    table_name: str

class RestAPIConfig(BaseModel):
    host: str
    port: int

class CarInventoryApiConfig(BaseModel):
    url_get_car: str
    url_update_status: str

class Config(BaseModel):
    database: PostgresqlConfig
    logging : LoggerConfig
    server_api : RestAPIConfig
    car_inventory_api : CarInventoryApiConfig
    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
    )