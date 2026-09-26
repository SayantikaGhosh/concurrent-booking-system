from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.booking import Booking
from datetime import datetime, timezone

def create_booking(db: Session, user_id, table_id, time_range, status: str, expiry_time) -> Booking:
    booking = Booking(
        user_id=user_id,
        table_id=table_id,
        time_range=time_range,
        status=status,
        expiry_time=expiry_time,
    )
    db.add(booking)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise
    db.refresh(booking)
    return booking

def update_booking_status(db: Session, booking_id, new_status):
    target_booking = db.query(Booking).filter(Booking.booking_id == booking_id).first()
    if target_booking:
        target_booking.status = new_status
        db.commit()
        return target_booking
    else:
        return None


def cancel_expired_bookings(db: Session) -> int:
    expired_bookings = db.query(Booking).filter(
        Booking.status == "pending",
        Booking.expiry_time < datetime.now(timezone.utc)
    ).all()

    for booking in expired_bookings:
        booking.status = "cancelled"

    db.commit()
    return len(expired_bookings)