from sqlalchemy import create_engine, JSON
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column
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


int_pk = Annotated[int, mapped_column(primary_key=True, comment="主键")]


class Json1(Base):
    # 表名
    __tablename__ = "json1"

    # 使用 Mapped 类型注解，和 Column 一样，可以指定列的类型和其他属性
    id: Mapped[int_pk]
    messages: Mapped[list[dict]] = mapped_column(
        JSONB if database_type == "postgresql" else JSON, comment="消息内容"
    )

    def __repr__(self):
        return f"<Json1(id={self.id}, messages={self.messages})>"


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
