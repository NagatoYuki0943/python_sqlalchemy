from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, func
from sqlalchemy.orm import declarative_base, sessionmaker


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


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, comment="主键")
    name = Column(String(128), unique=True, nullable=False, comment="姓名")
    birthday = Column(Date, nullable=False, comment="出生日期")
    address = Column(String(255), nullable=True, comment="地址")
    created_at = Column(
        DateTime, nullable=False, server_default=func.now(), comment="创建时间"
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
        comment="更新时间",
    )


# https://www.perplexity.ai/search/import-datetime-from-sqlalchem-o4auT4oDSgKu2q4MTMDeKA
# default 和 server_default
#     执行位置：
#         default: 在SQLAlchemy客户端执行，由Python生成默认值。
#         server_default: 在数据库服务器端执行，由数据库生成默认值。

#     SQL语句生成：
#         default: 默认值会被包含在INSERT语句中。
#         server_default: 默认值会被包含在CREATE TABLE语句中。
#     适用场景：
#         default: 适用于数据库不支持的复杂表达式或不想修改数据库模式时。
#         server_default: 确保所有客户端使用相同的默认值，适用于跨平台场景。

#     性能考虑：
#         default: 可能需要额外的Python处理时间。
#         server_default: 可能节省网络带宽，因为不需要发送该列的数据到数据库。

# onupdate 和 server_onupdate
#     执行位置：
#         onupdate: 在SQLAlchemy客户端执行，由Python生成更新值。
#         server_onupdate: 在数据库服务器端执行，由数据库生成更新值。
#     自动更新行为：
#         onupdate: SQLAlchemy可能需要额外的SELECT查询来获取更新后的值。
#         server_onupdate: 通常与FetchedValue()一起使用，可以利用RETURNING子句直接获取更新后的值。
#     使用方式：
#         onupdate: 直接使用，如onupdate=func.now()。
#         server_onupdate: 通常需要与FetchedValue()结合使用，如server_onupdate=FetchedValue()。
#     RETURNING子句的使用：
#         onupdate: 不会自动使用RETURNING子句。
#         server_onupdate: 与FetchedValue()结合使用时，会自动包含在RETURNING子句中。


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
