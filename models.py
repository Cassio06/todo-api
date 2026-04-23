
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer,primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique = True, nullable = False)
    password = Column(String(30), unique = False, nullable = False)

class Task(Base):
    __tablename__ = 'Tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(70), unique = True, nullable = False)
    description = Column(String(200), unique = False, nullable = False)
    completed = Column(Boolean, default = False, nullable = False)
    owner_id = Column(Integer,ForeignKey("users.id"), unique = True, nullable = False)


