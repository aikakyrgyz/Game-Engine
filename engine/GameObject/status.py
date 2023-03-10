from typing import Dict
from enum import Enum


class Status(Enum):
    FALLING = "falling"
    FALLEN = "fallen"


class Position(Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
# Dot notation
# Status.FALLING
# Output: <Status.FALLING: 'falling'>
