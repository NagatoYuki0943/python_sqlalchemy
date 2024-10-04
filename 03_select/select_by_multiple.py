from db_init import engine, person_table
from sqlalchemy.sql import and_, or_


with engine.connect() as conn:
    query = (
        person_table.select()
        .where(person_table.c.birthday > "2000-10-13")
        .where(person_table.c.id < 5)
    )
    result_set = conn.execute(query)

    rows = result_set.all()
    print(rows)
print("-" * 100)
# [(3, 'Mary', datetime.date(2000, 10, 14)), (4, 'Smith', datetime.date(2000, 10, 15))]


with engine.connect() as conn:
    # query = person_table.select().where(person_table.c.birthday > '2000-10-13').where(person_table.c.id < 6)
    query = person_table.select().where(
        or_(
            person_table.c.name == "Tom",
            and_(person_table.c.birthday > "2000-10-13", person_table.c.id < 5),
        )
    )
    result_set = conn.execute(query)

    rows = result_set.all()
    print(rows)
# [(1, 'Tom', datetime.date(2000, 10, 11)), (3, 'Mary', datetime.date(2000, 10, 14)), (4, 'Smith', datetime.date(2000, 10, 15))]
