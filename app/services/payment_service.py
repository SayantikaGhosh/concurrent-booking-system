from sqlalchemy.orm import Session

from app.repositories.payment_repository import create_payment
from app.repositories.booking_repository import update_booking_status

class BookingNotFoundError(Exception):
    pass


def process_payment(db: Session, booking_id, outcome: str):
    new_booking_status = "confirmed" if outcome == "succeeded" else "cancelled"

    updated_booking = update_booking_status(db, booking_id, new_booking_status)
    if updated_booking is None:
        raise BookingNotFoundError(f"No booking found with id {booking_id}")

    payment = create_payment(db, booking_id=booking_id, status=outcome)

    return payment, updated_booking