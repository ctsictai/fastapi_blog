from datetime import datetime
from pytz import timezone
from ..core.config import Base
from .user import User
from sqlalchemy import Column, ForeignKey, Integer, String, DATETIME, Text


class Board(Base):
    __tablename__ = "board"

    id = Column(Integer(unsigned=True), primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=True)
    context = Column(Text, nullable=True)
    created_at = Column(DATETIME, default=datetime.now(tz=timezone("utc")))
    author = Column(Integer(unsigned=True), ForeignKey(User.id, ondelete="DO NOTHING"))

    def __repr__(self):
        return "<Board(title='%s', author='%s'')>" % (self.title, self.author)
