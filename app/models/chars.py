from typing import Optional

from sqlalchemy import Column, Enum, Integer, String

from app.dto.enum import CharacterClassEnum

from ..db.base_class import Base


class Character(Base):
    """Character database mapping class"""

    id: Integer = Column(Integer, primary_key=True, index=True, autoincrement=True)
    """id character"""

    name: str = Column(String, index=True)
    """name"""

    object_link: Optional[str] = Column(String, nullable=True)
    """3d model"""

    character_image: str = Column(String)
    """image"""

    character_class: CharacterClassEnum = Column(Enum(CharacterClassEnum))
    """class"""

    description: str = Column(String)
    """description"""
