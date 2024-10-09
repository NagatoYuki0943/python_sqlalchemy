from sqlalchemy.orm import Mapped, relationship
from ..database_utils import (
    Base,
    int_pk,
    required_unique_string,
    string,
    text,
    timestamp_default_now,
    timestamp_update_now,
)
from ..conversations import Conversation


class Model(Base):
    __tablename__ = "chatbot_models"

    id: Mapped[int_pk]
    model_name: Mapped[required_unique_string]
    version: Mapped[string]
    desc: Mapped[text]
    status: Mapped[string]
    created_at: Mapped[timestamp_default_now]
    updated_at: Mapped[timestamp_update_now]

    # 关联字段
    conversations: Mapped[list[Conversation]] = relationship(
        Conversation, back_populates="model"
    )

    def __repr__(self):
        return f"<Model(id={self.id}, model_name='{self.model_name}', version='{self.version}', desc='{self.desc}', status='{self.status}')>"
