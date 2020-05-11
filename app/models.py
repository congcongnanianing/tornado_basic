from sqlalchemy import Column, Integer, String

from utils.conn import Base


def create_db():
    # 映射模型对应的表[定义的位置必须和模型定义在一个文件]
    Base.metadata.create_all()


def drop_db():
    # 删除模型映射的表
    Base.metadata.drop_all()


class Student(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    s_name = Column(String(10), unique=True, nullable=False)
    s_age = Column(Integer, default=18)

    __tablename__ = 'student'

    def __str__(self):
        return self.s_name
