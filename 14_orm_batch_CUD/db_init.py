import datetime

from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import Annotated


# database://username:password@hostname:port/database_name
database_type = "postgresql"
if database_type == "mysql":
    url = "mysql://root:root@localhost:3306/mb"
elif database_type == "postgresql":
    url = "postgresql://postgres:postgres@localhost:5432/mb"
else:
    raise ValueError("Unsupported database type")

# echo=True: 显示执行的SQL语句
engine = create_engine(url, echo=True)


int_pk = Annotated[int, mapped_column(primary_key=True)]
required_unique_string = Annotated[
    str, mapped_column(String(128), unique=True, nullable=False)
]
required_string = Annotated[str, mapped_column(String(128), nullable=False)]
timestamp_not_null = Annotated[datetime.datetime, mapped_column(nullable=False)]


class Base(DeclarativeBase):
    pass


class Department(Base):
    __tablename__ = "department"

    id: Mapped[int_pk]
    name: Mapped[required_unique_string]

    employees: Mapped[list["Employee"]] = relationship(
        "Employee", back_populates="department"
    )

    def __repr__(self):
        return f"department: id: {self.id}, name: {self.name}"


class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[int_pk]
    department_id: Mapped[int] = mapped_column(ForeignKey("department.id"))
    name: Mapped[required_unique_string]
    birthday: Mapped[timestamp_not_null]

    department: Mapped[Department] = relationship(
        Department, back_populates="employees"
    )

    def __repr__(self):
        return f"employee: id: {self.id}, dep_id: {self.dep_id}, name: {self.name}, birthday: {self.birthday}"


Base.metadata.create_all(engine)
