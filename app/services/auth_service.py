from sqlalchemy.orm import Session

from app.core.security import verify_password, create_access_token
from app.repositories.user_repository import get_user_by_email


class InvalidCredentialsError(Exception):
    pass


def login_user(db: Session, email: str, password: str) -> str:
    user = get_user_by_email(db, email)
    if user is None or not verify_password(password, user.password_hash):
        raise InvalidCredentialsError("Invalid email or password")

    return create_access_token(user_id=str(user.user_id))