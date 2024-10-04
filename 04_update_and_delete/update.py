from db_init import engine, person_table


with engine.connect() as conn:
    # update_query = person_table.update().values(address="Beijing")
    # where 查询条件不存在不会报错
    update_query = (
        person_table.update().values(address="Shanghai").where(person_table.c.id == 6)
    )
    conn.execute(update_query)
    conn.commit()
