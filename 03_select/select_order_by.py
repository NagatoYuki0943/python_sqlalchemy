from db_init import engine, person_table


# order_by() 排序, 默认升序
with engine.connect() as conn:
    query = person_table.select().order_by(person_table.c.id)
    result_set = conn.execute(query)
    print(result_set.keys())
    # RMKeyView(['id', 'name', 'birthday'])
    for row in result_set:
        print(row[0], row.name, row.birthday)
print("-" * 20)
# 1 Tom 2000-10-11
# 2 Jack 2000-10-13
# 3 Mary 2000-10-14
# 4 Smith 2000-10-15
# 5 Luck 2000-10-16
# 6 Jerry 2000-10-17
# 8 Amy 2000-09-18
# 9 Eric 1998-02-18
# 10 Samuel 1997-01-15


# order_by() 排序, 降序
with engine.connect() as conn:
    query = person_table.select().order_by(
        person_table.c.id.desc(), person_table.c.name.asc()
    )
    result_set = conn.execute(query)
    print(result_set.keys())
    # RMKeyView(['id', 'name', 'birthday'])
    for row in result_set:
        print(row[0], row.name, row.birthday)
print("-" * 20)
# 10 Samuel 1997-01-15
# 9 Eric 1998-02-18
# 8 Amy 2000-09-18
# 6 Jerry 2000-10-17
# 5 Luck 2000-10-16
# 4 Smith 2000-10-15
# 3 Mary 2000-10-14
# 2 Jack 2000-10-13
# 1 Tom 2000-10-11
