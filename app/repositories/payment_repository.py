from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.payment import Payment
from app.models.booking import Booking



def create_payment(db: Session, booking_id,  status: str, ) -> Payment:
    payment = Payment(
        booking_id = booking_id,
        status=status,
    )
    db.add(payment)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise
    db.refresh(payment)
    return payment

def update_booking_status(db: Session, booking_id, new_status):
    target_booking = db.query(Booking).filter(Booking.booking_id == booking_id).first()
    if target_booking:
        target_booking.status = new_status
        db.commit()
        return target_booking
    else:
        return None