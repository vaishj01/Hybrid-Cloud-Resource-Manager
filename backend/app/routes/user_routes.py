from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User

from app.schemas.user_schema import (
    UserCreate,
    UserResponse,
    UserUpdate,
    Token
)

from app.services.user_service import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user,
    login_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# -------------------------------
# Register User
# -------------------------------
@router.post("/register", response_model=UserResponse)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    new_user = create_user(db, user)

    if new_user is None:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return new_user


# -------------------------------
# Login User
# -------------------------------
@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    token = login_user(
        db,
        form_data.username,
        form_data.password
    )

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return token


# -------------------------------
# Get All Users (Protected)
# -------------------------------
@router.get("/", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_all_users(db)


# -------------------------------
# Get User By ID (Protected)
# -------------------------------
@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    user = get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# -------------------------------
# Update User (Protected)
# -------------------------------
@router.put("/{user_id}", response_model=UserResponse)
def update_existing_user(
    user_id: int,
    updated_user: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    user = update_user(db, user_id, updated_user)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# -------------------------------
# Delete User (Protected)
# -------------------------------
@router.delete("/{user_id}", response_model=UserResponse)
def delete_existing_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    user = delete_user(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user