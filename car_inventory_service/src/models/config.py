from typing import Literal, Optional, Any
from pydantic import BaseModel, PostgresDsn, ConfigDict


class LoggerConfig(BaseModel):
    logger_name: str
    logging_dict: dict[str, Any]
    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
    )

class PostgresqlConfig(BaseModel):
    database_type: Literal["postgresql"]
    connection_string: PostgresDsn
    table_name: str

class RestAPIConfig(BaseModel):
    port: int

class Config(BaseModel):
    database: PostgresqlConfig
    logging : LoggerConfig
    restapi : RestAPIConfig
    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
    )