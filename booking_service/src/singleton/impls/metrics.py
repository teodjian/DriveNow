from prometheus_client import Counter, Gauge, Histogram

class BookingMetrics:
    def __init__(self):
        # Gauge: "How many cars do we have right now?"
        # We use labels so we can filter by status (available/rented) and model (Toyota/Tesla)
        self.active_rentals = Gauge(
            'booking_active_rentals_total',
            'Number of rentals currently in progress',

        )
        self.total_rentals = Counter(
            'booking_cars_rented_total',
            'Total number of car rentals created since startup',
        )

        self.missed_rentals = Counter(
            'booking_missed_rentals_total',
            'Number of missed rentals, that cars are already rent',
        )