from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine


Base = declarative_base()


association_table = Table('authors', Base.metadata,
        Column('user_id', Integer, ForeignKey('users.id')),
        Column('project_id', Integer, ForeignKey('projects.id'))
    )


class User(Base):
    """
    user
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String)


class Profile(Base):
    """
    profile model"""
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    bio = Column(String)
    phone = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    user = relationship('User', backref='profiles', uselist=False)
    project = relationship('Project', secondary=association_table, back_populates='user')

class Project(Base):
    """
    project model
    """
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description  = Column(String)
    task = relationship('Tasks', backref='projects', uselist=False)
    user = relationship('User', secondary=association_table, back_populates='project')

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, unique=True)
    status = Column(String(255), nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)

engine = create_engine("sqlite:///test.db")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
ойо