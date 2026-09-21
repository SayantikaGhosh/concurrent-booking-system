from sqlalchemy.exc import IntegrityError

from app.core.config import settings
from app.repositories.booking_repository import create_booking
from app.models.booking import Booking
from app.models.table import RestaurantTable
from app.schemas.book_table import BookTableRequest, BookTableResponse
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from psycopg2.extras import DateTimeTZRange


class TableUnavailableError(Exception):
    pass


def book_table(db: Session, request: BookTableRequest, user_id: str) -> Booking:
    start_datetime = datetime.combine(request.date, request.start_time).replace(tzinfo=timezone.utc)
    end_datetime = datetime.combine(request.date, request.end_time).replace(tzinfo=timezone.utc)
    time_range = DateTimeTZRange(start_datetime, end_datetime)
    expiry_time = datetime.now(timezone.utc) + timedelta(minutes=settings.booking_hold_minutes)

    try:
        booking = create_booking(
            db,
            user_id=user_id,
            table_id=request.table_id,
            time_range=time_range,
            status="pending",
            expiry_time=expiry_time,
        )
    except IntegrityError:
        raise TableUnavailableError("This table is already booked for the requested time")

    return booking