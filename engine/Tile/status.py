from typing import Dict
from enum import Enum


class Status(Enum):
    FALLING = "falling"
    FROZEN = "frozen"
    FALLEN = "fallen"
    MATCHED = "matched"
    STILL = "still"
    


# Dot notation
# Status.FALLING
# Output: <Status.FALLING: 'falling'>
