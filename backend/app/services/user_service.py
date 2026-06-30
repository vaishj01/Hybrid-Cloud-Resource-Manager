from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.auth.password import hash_password, verify_password
from app.security.jwt_handler import create_access_token


def create_user(db: Session, user: UserCreate):

    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        return None

    # Hash the password
    hashed_password = hash_password(user.password)

    # Create a new User object
    new_user = User(
        full_name=user.full_name,
        email=user.email,
        password=hashed_password
    )

    # Save to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_all_users(db: Session):

    users = db.query(User).all()

    return users

def get_user_by_id(db: Session, user_id: int):

    user = db.query(User).filter(User.id == user_id).first()

    return user

def update_user(db: Session, user_id: int, updated_user):

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        return None

    user.full_name = updated_user.full_name
    user.email = updated_user.email

    db.commit()
    db.refresh(user)

    return user

def delete_user(db: Session, user_id: int):

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        return None

    db.delete(user)
    db.commit()

    return user

def login_user(
    db: Session,
    email: str,
    password: str
):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if user is None:
        return None

    if not verify_password(
        password,
        user.password
    ):
        return None

    access_token = create_access_token(
        {
            "sub": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }