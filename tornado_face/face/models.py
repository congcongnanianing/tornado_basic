from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime

from tornado_face.utils.conn import Base


def init_db():
    Base.metadata.create_all()


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(10), unique=True, nullable=False)
    realname = Column(String(10), unique=True, nullable=False)
    create_time = Column(DateTime, default=datetime.now())

    __tablename__ = 'user'
