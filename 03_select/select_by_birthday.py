from db_init import engine, person_table


with engine.connect() as conn:
    query = person_table.select().where(person_table.c.birthday > "2000-10-13")
    result_set = conn.execute(query)

    rows = result_set.all()
    print(rows)
# [(3, 'Mary', datetime.date(2000, 10, 14)), (4, 'Smith', datetime.date(2000, 10, 15)), (5, 'Luck', datetime.date(2000, 10, 16))]
