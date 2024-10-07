import sqlalchemy

engine = sqlalchemy.create_engine("mysql://root:root@localhost:3306/mb", echo=True)
engine = sqlalchemy.create_engine("postgresql://postgres:postgres@localhost:5432/mb", echo=True)

# 表数据定义存档在meta_data对象中
meta_data = sqlalchemy.MetaData()

# 创建 students 表
person_table = sqlalchemy.Table(
    "person",
    meta_data,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, comment="主键"),
    sqlalchemy.Column("name", sqlalchemy.String(128), unique=True, nullable=False, comment="姓名"),
    sqlalchemy.Column("birthday", sqlalchemy.Date, nullable=False, comment="出生日期"),
    sqlalchemy.Column("address", sqlalchemy.String(255), nullable=True, comment="地址"),
    sqlalchemy.Column("create_time", sqlalchemy.DateTime, nullable=False, server_default=sqlalchemy.func.now(), comment="创建时间"),
    sqlalchemy.Column("update_time", sqlalchemy.DateTime, nullable=False, server_default=sqlalchemy.func.now(), onupdate=sqlalchemy.func.now(), comment="更新时间"),
)
# https://www.perplexity.ai/search/import-datetime-from-sqlalchem-o4auT4oDSgKu2q4MTMDeKA
# default 和 server_default
#     执行位置：
#         default: 在SQLAlchemy客户端执行，由Python生成默认值1。
#         server_default: 在数据库服务器端执行，由数据库生成默认值1。

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


# 创建表, 默认情况下, 不会尝试重新创建目标数据库中已经存在的表。
meta_data.create_all(engine)


# insert a record
# 返回一个 intert 语句对象
person_insert = person_table.insert()
print(person_insert)
# INSERT INTO person (id, name, birthday) VALUES (:id, :name, :birthday)

insert_tom = person_insert.values(name="Tom", birthday="2000-10-11")

with engine.connect() as conn:
    # 传入 insert 语句
    result = conn.execute(insert_tom)
    print(result)
    print(result.inserted_primary_key)
    conn.commit()
# <sqlalchemy.engine.cursor.CursorResult object at 0x0000015CF1322580>
# (1,)


# insert multiple records
person_insert = person_table.insert()

with engine.connect() as conn:
    # 传入 insert 对象和参数字典
    result = conn.execute(
        person_insert,
        [
            {"name": "Jack", "birthday": "2000-10-13"},
            {"name": "Mary", "birthday": "2000-10-14"},
            {"name": "Smith", "birthday": "2000-10-15"},
            {"name": "Luck", "birthday": "2000-10-16"},
            {"name": "Jerry", "birthday": "2000-10-17"},
        ],
    )
    print(result)
    # 多条插入返回的结果为一个元组列表，每个元组对应一条插入记录的插入结果
    print(result.inserted_primary_key_rows)
    conn.commit()
# <sqlalchemy.engine.cursor.CursorResult object at 0x0000015CF1322510>
# [(None,), (None,), (None,)]

# 返回 id 为 None 的原因
# 原因解释
#     批量插入优化：多条记录插入通常被优化为一个批量操作，以提高性能。这种优化可能导致无法立即获取每条记录的插入ID.
#     数据库差异：不同的数据库在批量插入时返回自动生成ID的行为可能不同。有些数据库可能不支持在批量插入后立即返回所有生成的ID.
#     性能考虑：为了获取每条记录的ID，可能需要额外的数据库查询，这会降低批量插入的性能优势.

# 解决方案
# 如果你确实需要获取批量插入的ID，可以考虑以下方法：
#     单独插入：如果记录数量不多，可以考虑逐条插入，这样可以获取每条记录的ID.
#     使用返回值：某些数据库（如PostgreSQL）支持RETURNING子句，可以在插入时返回生成的ID。SQLAlchemy支持这一特性.
#     后续查询：在批量插入后，可以执行一个额外的查询来获取刚插入的记录ID.
#     使用ORM：如果使用SQLAlchemy的ORM层，它提供了更多的选项来处理这种情况.

# 总之，批量插入时无法直接获取ID是由于性能优化和数据库兼容性考虑造成的。根据具体需求，可以选择适当的方法来解决这个问题。
