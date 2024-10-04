from db_init import engine, person_table


# fetchone() 获取一条数据
with engine.connect() as conn:
    query = person_table.select()
    result_set = conn.execute(query)

    row = result_set.fetchone()
    print(row)
print("-" * 20)
# (1, 'Tom', datetime.date(2000, 10, 11))


# first() 获取第一条数据
with engine.connect() as conn:
    query = person_table.select()
    result_set = conn.execute(query)

    row = result_set.first()
    print(row)
print("-" * 20)
# (1, 'Tom', datetime.date(2000, 10, 11))


# one() 获取一条数据, 找到多条数据或者找不到数据时, 会抛出异常
with engine.connect() as conn:
    query = person_table.select().where(person_table.c.id == 2)
    result_set = conn.execute(query)
    # 找不到数据时, one() 会抛出异常, 多条数据时, one() 会抛出异常
    row = result_set.one()
    print(row)
print("-" * 20)
# (2, 'Jack', datetime.date(2000, 10, 13))


# one_or_none() 获取一条数据, 找到多条数据时报错, 找不到数据时返回None
with engine.connect() as conn:
    query = person_table.select().where(person_table.c.id == 25)
    result_set = conn.execute(query)
    row = result_set.one_or_none()
    print(row)
print("-" * 20)
# None


# 只返回指定的字段
with engine.connect() as conn:
    query = person_table.select().with_only_columns(
        person_table.c.id, person_table.c.name
    )
    result_set = conn.execute(query)

    row = result_set.first()
    print(row)
print("-" * 20)
# (8, 'Amy')
