from pydantic import BaseModel


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