from typing import Optional
from uuid import UUID

from sqlalchemy import Column, String

from db.base_class import Base
from db.sqltypes.uuid import UUIDType


class Character(Base):
    """Character database mapping class"""

    id: UUID = Column(
        UUIDType,
        primary_key=True,
        index=True,
    )
    """id character"""

    name: str = Column(String, index=True)
    """character name"""

    object_link: Optional[str] = Column(String, nullable=True)
    """character 3d model"""
