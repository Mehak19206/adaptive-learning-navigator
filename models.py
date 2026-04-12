from pydantic import BaseModel
from typing import Literal

class Observation(BaseModel):
    knowledge: float
    time_spent: float

class Action(BaseModel):
    action: Literal["easy", "medium", "hard", "revise", "skip"]

class Reward(BaseModel):
    value: float
