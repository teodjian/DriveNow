import yaml
from car_inventory_service.src.models.config import Config

def load_config(config_path: str) -> Config:
    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
            return Config(**config)
    except FileNotFoundError:
        raise FileNotFoundError(f"config file {config_path} not found")
