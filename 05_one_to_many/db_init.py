import sqlalchemy


# database://username:password@hostname:port/database_name
database_type = "postgresql"
if database_type == "mysql":
    url = "mysql://root:root@localhost:3306/mb"
elif database_type == "postgresql":
    url = "postgresql://postgres:postgres@localhost:5432/mb"
else:
    raise ValueError("Unsupported database type")

# echo=True: 显示执行的SQL语句
engine = sqlalchemy.create_engine(url, echo=True)

meta_data = sqlalchemy.MetaData()

department = sqlalchemy.Table(
    "department",
    meta_data,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(255), nullable=False, unique=True),
)

employee = sqlalchemy.Table(
    "employee",
    meta_data,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    # 外键约束
    sqlalchemy.Column(
        "department_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("department.id"),
        nullable=False,
    ),
    sqlalchemy.Column("name", sqlalchemy.String(255), nullable=False),
    sqlalchemy.Column("birthday", sqlalchemy.DateTime, nullable=False),
)

meta_data.create_all(engine)
