"""
Models
"""

from dataclasses import dataclass
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from db import engine

Base = declarative_base()

association_table = Table('authors', Base.metadata,
        Column('user_id', Integer, ForeignKey('users.id')),
        Column('project_id', Integer, ForeignKey('projects.id'))
    )

@dataclass
class User(Base):
    """
    user
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255))
    projects = relationship('Project', secondary=association_table, back_populates='users')

@dataclass
class Profile(Base):
    """
    profile model
    """
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    bio = Column(String)
    phone = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    user = relationship('User', backref='profile', uselist=False)

@dataclass
class Project(Base):
    """
    project model
    """
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    description  = Column(String)
    # task = relationship('Tasks', backref='projects', uselist=False)
    users = relationship('User', secondary=association_table, back_populates='projects')

@dataclass
class Task(Base):
    """
    task model
    """
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, unique=True)
    status = Column(String(255), nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    project = relationship('Project', backref='task', uselist=False)

# engine = create_engine("sqlite:///test.db")

# if __name__ == "__main__":
Base.metadata.create_all(engine)
