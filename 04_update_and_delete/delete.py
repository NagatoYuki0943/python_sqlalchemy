from db_init import engine, person_table


with engine.connect() as conn:
    # 删除所有记录
    # delete_query = person_table.delete()
    # where 查询条件不存在不会报错
    delete_query = person_table.delete().where(person_table.c.id == 7)
    conn.execute(delete_query)
    conn.commit()
