from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("mysql://root:root@localhost:3306/mb", echo=True)
engine = create_engine("postgresql://postgres:postgres@localhost:5432/mb", echo=True)
Base = declarative_base()


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, comment="主键")
    name = Column(String(128), unique=True, nullable=False, comment="姓名")
    birthday = Column(Date, nullable=False, comment="出生日期")
    address = Column(String(255), nullable=True, comment="地址")


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
