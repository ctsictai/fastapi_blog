from ..core.config import Base
from sqlalchemy import Column, Integer, String, Boolean

class FooItem(Base):
    __tablename__ = "foo_items"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    public = Column(Boolean, default=False)