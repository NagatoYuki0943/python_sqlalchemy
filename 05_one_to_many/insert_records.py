from db_init import engine, department, employee

with engine.connect() as conn:
    conn.execute(department.insert(), [{"name": "hr"}, {"name": "it"}])

    conn.execute(
        employee.insert(),
        [
            {"department_id": 1, "name": "Jack", "birthday": "1990-01-01 12:00:00"},
            {"department_id": 1, "name": "Tom", "birthday": "1990-01-02 13:00:00"},
            {"department_id": 1, "name": "Mary", "birthday": "1990-01-03 14:00:00"},
            {"department_id": 2, "name": "Smith", "birthday": "1990-01-04 9:00:00"},
            {"department_id": 2, "name": "Rose", "birthday": "1990-01-05 10:00:00"},
            {"department_id": 2, "name": "Leon", "birthday": "1990-01-06 18:00:00"},
        ],
    )

    conn.commit()
