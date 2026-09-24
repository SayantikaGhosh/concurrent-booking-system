import uuid
from pydantic import BaseModel
from typing import Literal


class PaymentRequest(BaseModel):
    outcome: Literal["succeeded", "failed"]  


class PaymentResponse(BaseModel):
    payment_id: uuid.UUID
    payment_status: Literal["succeeded", "failed"]
    booking_status: Literal["confirmed", "cancelled"]