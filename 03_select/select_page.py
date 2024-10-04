from db_init import engine, person_table


# offset() limit() 分页
with engine.connect() as conn:
    query = person_table.select().offset(1).limit(2)
    result_set = conn.execute(query)
    print(result_set.keys())
    # RMKeyView(['id', 'name', 'birthday'])
    for row in result_set:
        print(row[0], row.name, row.birthday)
print("-" * 20)
# 2 Jack 2000-10-13
# 3 Mary 2000-10-14
