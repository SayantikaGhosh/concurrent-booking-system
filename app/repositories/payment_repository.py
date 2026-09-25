from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.payment import Payment

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

