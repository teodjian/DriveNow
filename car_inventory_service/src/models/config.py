from typing import Literal, Optional
from pydantic import BaseModel, PostgresDsn, ConfigDict


class LoggerConfig(BaseModel):
    logger_name: str
    log_level: str = "INFO"
    enable_console: bool = True
    log_file_path: Optional[str] = None

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