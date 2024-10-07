from sqlalchemy import create_engine, String, ForeignKey, Table, Column
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    Mapped,
    mapped_column,
    relationship,
)
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

Base = declarative_base()


int_pk = Annotated[int, mapped_column(primary_key=True)]
required_unique_name = Annotated[
    str, mapped_column(String(128), unique=True, nullable=False)
]
required_string = Annotated[str, mapped_column(String(128), nullable=False)]


# 中间表,没有使用类,因为用不到
association_table = Table(
    "user_role",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int_pk]
    name: Mapped[required_unique_name]
    password: Mapped[required_string]

    # 参数1: 关联的类名, 在使用了 Mapped[] 后, 这里可以不需要再写具体的类名了
    # secondary 定义中间表, lazy=False 表示延迟加载, back_populates 定义反向关系
    # back_populates 可以为None
    roles: Mapped[list["Role"]] = relationship(
        "Role", secondary=association_table, lazy=False, back_populates="users"
    )

    def __repr__(self):
        return f"user: id: {self.id}, name: {self.name}"


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int_pk]
    name: Mapped[required_unique_name]

    # 参数1: 关联的类名, 在使用了 Mapped[] 后, 这里可以不需要再写具体的类名了
    # secondary 定义中间表, lazy=True 表示关闭延迟加载, back_populates 定义反向关系
    # back_populates 可以为None
    users: Mapped[list["User"]] = relationship(
        User, secondary=association_table, lazy=True, back_populates="roles"
    )

    def __repr__(self):
        return f"role: id: {self.id}, name: {self.name}"


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
