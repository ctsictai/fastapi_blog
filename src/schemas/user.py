from pydantic import BaseModel
from typing import Optional
from src.schemas.base_schemas import AllOptional


class BaseUser(BaseModel):
    id: int
    email: str
    password: str
    user_type: str


class UserModel(BaseModel, metaclass=AllOptional):
    user_name: str
