import uuid
from pydantic import BaseModel, EmailStr


class UserRegisterRequest(BaseModel):
    """What the client sends to POST /register."""
    name: str
    email: EmailStr
    phone_no: str
    password: str  


class UserResponse(BaseModel):
    """What we send back — never includes the password or its hash."""
    user_id: uuid.UUID
    name: str
    email: EmailStr
    phone_no: str

    class Config:
        from_attributes = True  