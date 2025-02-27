# from sqlalchemy.orm import declarative_base
# from sqlalchemy import Column, Integer, String, Boolean
# from db import engine

# Base = declarative_base()

# class Task(Base):
#     __tablename__ = "tasks"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(255), nullable=False, unique=True)
#     description = Column(String(255), nullable=False)
#     completed = Column(Boolean, default=False)

# Base.metadata.create_all(engine)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = "sqlite:///tasks.db"

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

