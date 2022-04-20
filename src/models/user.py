from ..core.config import Base
from sqlalchemy import Column, Integer, String, Boolean


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(unsigned=True), primary_key=True, index=True, autoincrement=True)
    email = Column(
        String(100),
    )
    password = Column(String(255))
    user_type = Column(String(50), default="EMAIL")
    user_name = Column(String(50), nullable=True)
