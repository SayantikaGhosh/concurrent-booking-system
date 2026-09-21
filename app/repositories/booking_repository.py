from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.booking import Booking


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