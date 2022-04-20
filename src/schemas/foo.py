## DTO or Repository
from pydantic import BaseModel
from typing import Optional

class FooItemBase(BaseModel):
    description: Optional[str]
    public : Optional[bool]
    favorite_count: int | None = 0 
    name : Optional[str]
    

class FooItemCreate(FooItemBase):
    public: bool
    
    class Config:
        orm_mode = True

class FooItem(FooItemBase):
    id: int

    class Config:
        orm_mode = True