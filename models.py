from sqlalchemy import create_engine, Column, Integer, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

Base = declarative_base()

class Conversation(Base):
    __tablename__ = 'conversations'
    id = Column(Integer, primary_key=True)
    data = Column(JSON)
    fetched_at = Column(DateTime, default=datetime.utcnow)

def get_engine(db_path=None):
    db_path = db_path or os.path.join('data', 'intercom.db')
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    return create_engine(f'sqlite:///{db_path}', connect_args={'check_same_thread': False})

engine = get_engine()
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
SessionLocal.configure(bind=engine)
