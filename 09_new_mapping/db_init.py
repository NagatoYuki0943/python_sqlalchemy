import datetime

from sqlalchemy import create_engine, String
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column
from sqlalchemy.sql import func
from typing import Annotated


engine = create_engine("mysql://root:root@localhost:3306/mb", echo=True)
Base = declarative_base()


int_pk = Annotated[int, mapped_column(primary_key=True)]
required_unique_name = Annotated[
    str, mapped_column(String(128), unique=True, nullable=False)
]
birthday_date = Annotated[datetime.date, mapped_column(nullable=True)]
# server_default: sql语句中的 default 关键字，数据库默认值
timestamp_default_now = Annotated[
    datetime.datetime, mapped_column(nullable=False, server_default=func.now())
]


class Customer(Base):
    __tablename__ = "customers"

    # 使用 Mapped 类型注解，和 Column 一样，可以指定列的类型和其他属性
    id: Mapped[int_pk]
    name: Mapped[required_unique_name]
    birthday: Mapped[birthday_date]
    city: Mapped[str] = mapped_column(String(128), nullable=True)
    create_time: Mapped[timestamp_default_now]


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
