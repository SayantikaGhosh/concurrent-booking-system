import uuid

from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base


class RestaurantTable(Base):
    __tablename__ = "tables"

    table_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    table_size = Column(Integer, nullable=False)