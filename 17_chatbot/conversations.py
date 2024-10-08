from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from base import (
    Base,
    int_pk,
    string,
    default_zero_int,
    json_type,
    timestamp_default_now,
    timestamp_update_now,
)
from typing import TYPE_CHECKING  # for type hinting, 可以解决循环导入问题

if TYPE_CHECKING:
    from users import User
    from models import Model


class Conversation(Base):
    __tablename__ = "chatbot_conversations"

    id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey("chatbot_users.id"))
    model_id: Mapped[int] = mapped_column(ForeignKey("chatbot_models.id"))
    messages: Mapped[json_type]
    input_tokens_sum: Mapped[default_zero_int]
    output_tokens_sum: Mapped[default_zero_int]
    status: Mapped[string]
    created_at: Mapped[timestamp_default_now]
    updated_at: Mapped[timestamp_update_now]

    # 关联字段
    user: Mapped["User"] = relationship("User", back_populates="conversations")
    model: Mapped["Model"] = relationship("Model", back_populates="conversations")

    def __repr__(self):
        return f"<Conversation(id={self.id}, user_id={self.user_id}, model_id={self.model_id}, messages={self.messages}, input_tokens_sum={self.input_tokens_sum}, output_tokens_sum={self.output_tokens_sum}, status='{self.status}')>"
