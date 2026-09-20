from sqlalchemy.orm import Session

from app.models.user import User


def create_user(db: Session, name: str, email: str, phone_no: str, password_hash: str) -> User:
    user = User(name=name, email=email, phone_no=phone_no, password_hash=password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()