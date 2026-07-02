from pydantic import BaseModel, ConfigDict


class ResourceBase(BaseModel):

    resource_name: str

    provider: str

    resource_type: str

    region: str

    status: str


class ResourceCreate(ResourceBase):
    pass


class ResourceUpdate(ResourceBase):
    pass


class ResourceResponse(ResourceBase):

    id: int

    owner_id: int

    class Config:
        from_attributes = True

class PaginatedResourceResponse(BaseModel):

    page: int

    size: int

    total_records: int

    total_pages: int

    items: list[ResourceResponse]

    model_config = ConfigDict(
        from_attributes=True
    )