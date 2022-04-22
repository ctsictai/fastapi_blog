from datetime import datetime
from pytz import timezone
from ..core.config import Base
from sqlalchemy import Column, Integer, String, DateTime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(unsigned=True), primary_key=True, index=True, autoincrement=True)
    email = Column(
        String(100),
    )
    password = Column(String(255))
    user_type = Column(String(50), default="EMAIL")
    user_name = Column(String(50), nullable=True)
    created_at = Column(DATETIME, default=datetime.now(tz=timezone("utc")))

    def __repr__(self):
        return "<User(email='%s', user_type='%s', user_name='%s')>" % (self.email, self.user_type, self.user_name)
