from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_users: int
    total_resources: int
    aws_resources: int
    azure_resources: int
    gcp_resources: int
    running_resources: int
    stopped_resources: int