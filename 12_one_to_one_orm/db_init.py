from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    Mapped,
    mapped_column,
    relationship,
)
from typing import Annotated


engine = create_engine("mysql://root:root@localhost:3306/mb", echo=True)
engine = create_engine("postgresql://postgres:postgres@localhost:5432/mb", echo=True)
Base = declarative_base()


int_pk = Annotated[int, mapped_column(primary_key=True)]
required_unique_string = Annotated[
    str, mapped_column(String(128), unique=True, nullable=False)
]
required_string = Annotated[str, mapped_column(String(128), nullable=False)]


class Employee(Base):
    __tablename__ = "computer_employee"

    id: Mapped[int_pk]
    name: Mapped[required_unique_string]
    computer_id: Mapped[int] = mapped_column(ForeignKey("computer.id"), nullable=True)

    # 参数1: 关联的类名, 在使用了 Mapped[] 后, 这里可以不需要再写具体的类名了
    computer: Mapped["Computer"] = relationship(
        "Computer", lazy=False, back_populates="employee"
    )

    def __repr__(self):
        return f"employee: id: {self.id}, name: {self.name}"


class Computer(Base):
    __tablename__ = "computer"

    id: Mapped[int_pk]
    model: Mapped[required_string]
    number: Mapped[required_unique_string]

    # 参数1: 关联的类名, 在使用了 Mapped[] 后, 这里可以不需要再写具体的类名了
    employee: Mapped[Employee] = relationship(
        Employee, lazy=True, back_populates="computer"
    )

    def __repr__(self):
        return f"computer: id: {self.id}, model: {self.model}, number: {self.number}"


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
