import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TSTZRANGE, ExcludeConstraint
from sqlalchemy.sql import func

from app.core.database import Base


class Booking(Base):
    __tablename__ = "bookings"

    booking_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    table_id = Column(UUID(as_uuid=True), ForeignKey("tables.table_id"), nullable=False)

    time_range = Column(TSTZRANGE, nullable=False)

    status = Column(String, nullable=False, default="pending")
    expiry_time = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        ExcludeConstraint(
            (table_id, "="),
            (time_range, "&&"),
            name="no_overlapping_bookings_per_table",
            using="gist",
            where="status != 'cancelled'",
        ),
    )