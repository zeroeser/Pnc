from enum import Enum


class CharacterClassEnum(str, Enum):
    berserk = "berserk"
    """Berserk"""
    medic = "medic"
    """Medic"""
    guardian = "guardian"
    """Guardian"""
    specialist = "specialist"
    """Specialist"""
    marksman = "marksman"
    """Marksman"""
