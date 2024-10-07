from db_init import engine, person_table


with engine.connect() as conn:
    query = person_table.select()
    result_set = conn.execute(query)
    print(result_set.keys())
    # RMKeyView(['id', 'name', 'birthday'])
    for row in result_set:
        print(row[0], row.name, row.birthday)
print("-" * 100)
# 1 Tom 2000-10-11
# 2 Jack 2000-10-13
# 3 Mary 2000-10-14
# 4 Smith 2000-10-15


# all() 获取全部数据
with engine.connect() as conn:
    query = person_table.select()
    result_set = conn.execute(query)
    rows = result_set.all()
    print(rows)
print("-" * 100)
# [(1, 'Tom', datetime.date(2000, 10, 11)), (2, 'Jack', datetime.date(2000, 10, 13)), (3, 'Mary', datetime.date(2000, 10, 14)), (4, 'Smith', datetime.date(2000, 10, 15))]


# all() 获取全部数据
with engine.connect() as conn:
    query = person_table.select()
    result_set = conn.execute(query)
    # fetchall() == all()
    rows = result_set.fetchall()
    print(rows)
print("-" * 100)
# [(1, 'Tom', datetime.date(2000, 10, 11)), (2, 'Jack', datetime.date(2000, 10, 13)), (3, 'Mary', datetime.date(2000, 10, 14)), (4, 'Smith', datetime.date(2000, 10, 15))]


# fetchmany() 获取n条数据
with engine.connect() as conn:
    query = person_table.select()
    result_set = conn.execute(query)

    row = result_set.fetchmany(2)
    print(row)
print("-" * 100)
# [(1, 'Tom', datetime.date(2000, 10, 11)), (2, 'Jack', datetime.date(2000, 10, 13))]
