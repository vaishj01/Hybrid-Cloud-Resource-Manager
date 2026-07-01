from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.user import User
from app.models.resource import Resource


def get_dashboard_stats(db: Session):

    total_users = db.query(User).count()

    total_resources = db.query(Resource).count()

    aws_resources = db.query(Resource).filter(
        Resource.provider == "AWS"
    ).count()

    azure_resources = db.query(Resource).filter(
        Resource.provider == "Azure"
    ).count()

    gcp_resources = db.query(Resource).filter(
        Resource.provider == "GCP"
    ).count()

    running_resources = db.query(Resource).filter(
        Resource.status == "Running"
    ).count()

    stopped_resources = db.query(Resource).filter(
        Resource.status == "Stopped"
    ).count()

    return {
        "total_users": total_users,
        "total_resources": total_resources,
        "aws_resources": aws_resources,
        "azure_resources": azure_resources,
        "gcp_resources": gcp_resources,
        "running_resources": running_resources,
        "stopped_resources": stopped_resources
    }
def get_provider_stats(db: Session):

    provider_stats = (
        db.query(
            Resource.provider,
            func.count(Resource.id)
        )
        .group_by(Resource.provider)
        .all()
    )

    return {
        provider: count
        for provider, count in provider_stats
    }

def get_status_stats(db: Session):

    status_stats = (
        db.query(
            Resource.status,
            func.count(Resource.id)
        )
        .group_by(Resource.status)
        .all()
    )

    return {
        status: count
        for status, count in status_stats
    }

def get_region_stats(db: Session):

    region_stats = (
        db.query(
            Resource.region,
            func.count(Resource.id)
        )
        .group_by(Resource.region)
        .all()
    )

    return {
        region: count
        for region, count in region_stats
    }

def get_my_resources(
    db: Session,
    current_user: User
):

    return db.query(Resource).filter(
        Resource.owner_id == current_user.id
    ).all()