from database import engine, Session
from base import Base
from users import User
from models import Model
from conversations import Conversation

# Create all tables
Base.metadata.create_all(engine)
