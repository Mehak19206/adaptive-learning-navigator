from pydantic import BaseModel

class Observation(BaseModel):
    knowledge: int
    time_spent: int

class Reward(BaseModel):
    value: float