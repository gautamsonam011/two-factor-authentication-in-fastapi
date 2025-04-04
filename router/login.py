import email
from database.models import User
from sqlalchemy.orm import Session

def get_login(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user