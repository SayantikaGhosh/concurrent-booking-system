from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.repositories.user_repository import create_user, get_user_by_email
from app.schemas.user import UserRegisterRequest
from app.models.user import User


class EmailAlreadyRegisteredError(Exception):
    pass


def register_user(db: Session, request: UserRegisterRequest) -> User:
    existing = get_user_by_email(db, request.email)
    if existing is not None:
        raise EmailAlreadyRegisteredError(f"Email {request.email} is already registered")

    password_hash = hash_password(request.password)
    return create_user(
        db,
        name=request.name,
        email=request.email,
        phone_no=request.phone_no,
        password_hash=password_hash,
    )