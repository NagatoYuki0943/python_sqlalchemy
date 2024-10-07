import sqlalchemy

engine = sqlalchemy.create_engine("mysql://root:root@localhost:3306/mb", echo=True)
engine = sqlalchemy.create_engine("postgresql://postgres:postgres@localhost:5432/mb", echo=True)

meta_data = sqlalchemy.MetaData()

person_table = sqlalchemy.Table(
    "person",
    meta_data,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, comment="主键"),
    sqlalchemy.Column("name", sqlalchemy.String(128), unique=True, nullable=False, comment="姓名"),
    sqlalchemy.Column("birthday", sqlalchemy.Date, nullable=False, comment="出生日期"),
    sqlalchemy.Column("address", sqlalchemy.String(255), nullable=True, comment="地址"),
    sqlalchemy.Column("create_time", sqlalchemy.DateTime, nullable=False, default=sqlalchemy.func.now(), comment="创建时间"),
    sqlalchemy.Column("update_time", sqlalchemy.DateTime, nullable=False, default=sqlalchemy.func.now(), onupdate=sqlalchemy.func.now(), comment="更新时间"),
)

meta_data.create_all(engine)
