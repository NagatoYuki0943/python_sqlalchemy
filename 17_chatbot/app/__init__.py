from .core import engine, Session, Base  # Noqa
from .models import Conversation, Model, User  # Noqa


# Create all tables
Base.metadata.create_all(engine)
