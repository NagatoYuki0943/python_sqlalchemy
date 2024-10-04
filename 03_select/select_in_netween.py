from db_init import engine, person_table
from sqlalchemy.sql import between


with engine.connect() as conn:
    query = person_table.select().where(person_table.c.id.in_([3, 4, 5]))
    result_set = conn.execute(query)

    rows = result_set.all()
    print(rows)
print("-" * 100)
# [(3, 'Mary', datetime.date(2000, 10, 14)), (4, 'Smith', datetime.date(2000, 10, 15)), (5, 'Luck', datetime.date(2000, 10, 16))]


with engine.connect() as conn:
    query = person_table.select().where(person_table.c.id.between(3, 5))
    result_set = conn.execute(query)

    rows = result_set.all()
    print(rows)
print("-" * 100)
# [(3, 'Mary', datetime.date(2000, 10, 14)), (4, 'Smith', datetime.date(2000, 10, 15)), (5, 'Luck', datetime.date(2000, 10, 16))]


with engine.connect() as conn:
    query = person_table.select().where(between(person_table.c.id, 3, 5))
    result_set = conn.execute(query)

    rows = result_set.all()
    print(rows)
print("-" * 100)
# [(3, 'Mary', datetime.date(2000, 10, 14)), (4, 'Smith', datetime.date(2000, 10, 15)), (5, 'Luck', datetime.date(2000, 10, 16))]
