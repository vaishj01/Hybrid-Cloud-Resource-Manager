from sqlalchemy.orm import Session

from app.models.resource import Resource
from app.models.user import User

from app.schemas.resource_schema import (
    ResourceCreate,
    ResourceUpdate
)


def create_resource(
    db: Session,
    resource: ResourceCreate,
    current_user: User
):

    new_resource = Resource(
        resource_name=resource.resource_name,
        provider=resource.provider,
        resource_type=resource.resource_type,
        region=resource.region,
        status=resource.status,
        owner_id=current_user.id
    )

    db.add(new_resource)
    db.commit()
    db.refresh(new_resource)

    return new_resource


def get_all_resources(db: Session):

    return db.query(Resource).all()


def get_resource_by_id(
    db: Session,
    resource_id: int
):

    return db.query(Resource).filter(
        Resource.id == resource_id
    ).first()


def update_resource(
    db: Session,
    resource_id: int,
    updated_resource: ResourceUpdate
):

    resource = db.query(Resource).filter(
        Resource.id == resource_id
    ).first()

    if resource is None:
        return None

    resource.resource_name = updated_resource.resource_name
    resource.provider = updated_resource.provider
    resource.resource_type = updated_resource.resource_type
    resource.region = updated_resource.region
    resource.status = updated_resource.status

    db.commit()
    db.refresh(resource)

    return resource


def delete_resource(
    db: Session,
    resource_id: int
):

    resource = db.query(Resource).filter(
        Resource.id == resource_id
    ).first()

    if resource is None:
        return None

    db.delete(resource)
    db.commit()

    return resource