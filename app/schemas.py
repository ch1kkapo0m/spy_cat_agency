from typing import List, Optional
from pydantic import BaseModel

class TargetCreate(BaseModel):
    name: str
    country: str
    notes: str

class TargetUpdate(BaseModel):
    notes: Optional[str]
    is_complete: Optional[bool]

class TargetResponse(TargetCreate):
    id: int
    is_complete: bool

    class Config:
        orm_mode = True

class MissionCreate(BaseModel):
    targets: List[TargetCreate]

class MissionResponse(BaseModel):
    id: int
    is_completed: bool
    targets: List[TargetResponse]

    class Config:
        orm_mode = True

class CatCreate(BaseModel):
    name: str
    years_of_experience: int
    breed: str
    salary: float

class CatUpdate(BaseModel):
    salary: float

class CatResponse(BaseModel):
    id: int
    name: str
    years_of_experience: int
    breed: str
    salary: float

    class Config:
        orm_mode = True
