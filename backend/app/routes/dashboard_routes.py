from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.dashboard_schema import DashboardResponse

from app.services.dashboard_service import (
    get_dashboard_stats,
    get_provider_stats,
    get_status_stats,
    get_region_stats,
    get_my_resources
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/", response_model=DashboardResponse)
def dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_dashboard_stats(db)


@router.get("/providers")
def provider_statistics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_provider_stats(db)

@router.get("/status")
def status_statistics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_status_stats(db)

@router.get("/regions")
def region_statistics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_region_stats(db)

@router.get("/my-resources")
def my_resources(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_my_resources(
        db,
        current_user
    )