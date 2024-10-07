import datetime

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
required_unique_name = Annotated[
    str, mapped_column(String(128), unique=True, nullable=False)
]
timestamp_not_null = Annotated[datetime.datetime, mapped_column(nullable=False)]


class Department(Base):
    __tablename__ = "department"

    id: Mapped[int_pk]
    name: Mapped[required_unique_name]

    # 关联字段(一对多)
    # 参数1: 关联的类名, 在使用了 Mapped[] 后, 这里可以不需要再写具体的类名了
    # lazy="select" 默认加载方式, 当调用 employees 参数时, 才会查询数据库, 会产生多次加载
    # back_populates="department" 中的 department 字段需要在 Employee 类中定义 (2个类中都需要定义)
    # back_populates可以为None, 这样就是单向引用了
    employees: Mapped[list["Employee"]] = relationship(
        "Employee", back_populates="department"
    )

    def __repr__(self):
        return f"employee: id: {self.id}, name: {self.name}"


class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[int_pk]
    # 外键
    department_id: Mapped[int] = mapped_column(ForeignKey("department.id"))
    name: Mapped[required_unique_name]
    birthday: Mapped[timestamp_not_null]

    # 关联字段(多对一)
    # 参数1: 关联的类名, 在使用了 Mapped[] 后, 这里可以不需要再写具体的类名了
    # lazy=False 避免延迟加载, 使用联合查询,一次查询全部结果
    # back_populates="employees" 中的 employees 字段需要在 Department 类中定义 (2个类中都需要定义)
    department: Mapped[Department] = relationship(
        Department, lazy=False, back_populates="employees"
    )

    def __repr__(self):
        return f"department: id: {self.id}, department_id: {self.department_id}, name: {self.name}, birthday: {self.birthday}"


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
