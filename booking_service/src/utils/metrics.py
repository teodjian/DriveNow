from booking_service.src.singleton.impls.metrics import BookingMetrics


def add_rental():
    """
    Call this when a user successfully completes a booking.
    """
    # Increase the active count
    booking_metrics.active_rentals.inc()

    # Increment the total historical counter
    booking_metrics.total_rentals.inc()


def remove_rental():
    """
    Call this when the car is returned.
    """
    booking_metrics.active_rentals.dec()


booking_metrics = BookingMetrics()