from utils.hashing import Hasher
from database.models import User
from schemas.user import UserCreate
from sqlalchemy.orm import Session


def create_new_user(user: UserCreate, db: Session):
    user = User(
        email = user.email,
        hashed_password = Hasher.get_password_hash(user.password),
        conf_hashed_password = Hasher.get_password_hash(user.conf_password),
        secret = user.secret
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user
    