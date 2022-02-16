from ..core.config import Base
from sqlalchemy import Column, Integer, String, Boolean

class FooItem(Base):
    __tablename__ = "foo_items"

    id = Column(Integer(unsigned=True), primary_key=True, index=True, autoincrement=True)
    description = Column(String, nullable=True)
    public = Column(Boolean, default=False)
    favorite_count = Column(Integer(unsigned=True), default=0)
    name = Column(String(50), nullable=True)