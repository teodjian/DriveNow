from prometheus_client import Counter, Gauge, Histogram

class CarInventoryMetrics:
    def __init__(self):
        # Gauge: "How many cars do we have right now?"
        # We use labels so we can filter by status (available/rented) and model (Toyota/Tesla)
        self.car_inventory_gauge = Gauge(
            'car_inventory_total',
            'Current number of cars in inventory',
            ['status', 'model']
        )

        # Histogram: "How long are requests taking?"
        self.request_latency = Histogram(
            'inventory_request_latency_seconds',
            'Time spent processing inventory requests',
            ['method', 'endpoint']
        )