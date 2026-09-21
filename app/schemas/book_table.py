import uuid
from pydantic import BaseModel
from datetime import date , time, datetime

class BookTableRequest(BaseModel):
    table_id: uuid.UUID
    date: date
    start_time: time
    end_time: time

class BookTableResponse(BaseModel):
    booking_id: uuid.UUID
    status: str
    expiry_time: datetime
