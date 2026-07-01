from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.resource_schema import (
    ResourceCreate,
    ResourceUpdate,
    ResourceResponse
)

from app.services.resource_service import (
    create_resource,
    get_all_resources,
    get_resource_by_id,
    update_resource,
    delete_resource
)


router = APIRouter(
    prefix="/resources",
    tags=["Resources"]
)


@router.post("/", response_model=ResourceResponse)
def create_new_resource(
    resource: ResourceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_resource(
        db,
        resource,
        current_user
    )


@router.get("/", response_model=list[ResourceResponse])
def get_resources(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_all_resources(db)


@router.get("/{resource_id}", response_model=ResourceResponse)
def get_resource(
    resource_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    resource = get_resource_by_id(
        db,
        resource_id
    )

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="Resource not found"
        )

    return resource


@router.put("/{resource_id}", response_model=ResourceResponse)
def update_existing_resource(
    resource_id: int,
    updated_resource: ResourceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    resource = update_resource(
        db,
        resource_id,
        updated_resource
    )

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="Resource not found"
        )

    return resource


@router.delete("/{resource_id}", response_model=ResourceResponse)
def delete_existing_resource(
    resource_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    resource = delete_resource(
        db,
        resource_id
    )

    if resource is None:
        raise HTTPException(
            status_code=404,
            detail="Resource not found"
        )

    return resource