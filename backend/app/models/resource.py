from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class Resource(Base):
    __tablename__ = "resources"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    resource_name = Column(
        String,
        nullable=False
    )

    provider = Column(
        String,
        nullable=False
    )

    resource_type = Column(
        String,
        nullable=False
    )

    region = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        nullable=False
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    owner = relationship(
        "User",
        back_populates="resources"
    )