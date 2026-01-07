from car_inventory_service.src.models.car import CarStatus
from car_inventory_service.src.singleton.metrics import CarInventoryMetrics

inventory_metrics = CarInventoryMetrics()


def add_car_inventory_count(status: CarStatus, model: str):
    """Sets the gauge to the exact current number of cars."""
    inventory_metrics.car_inventory_gauge.labels(status=status, model=model).inc()


def remove_car_inventory_count(status: CarStatus, model: str):
    """Sets the gauge to the exact current number of cars."""
    inventory_metrics.car_inventory_gauge.labels(status=status, model=model).dec()


def observe_latency(method: str, endpoint: str, duration: float):
    """Record the duration of a request."""
    inventory_metrics.request_latency.labels(method=method, endpoint=endpoint).observe(duration)
