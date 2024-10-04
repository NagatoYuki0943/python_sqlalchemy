from sqlalchemy import select, insert, update, bindparam, delete
from sqlalchemy.orm import Session

from db_init import engine, Department, Employee


def batch_insert():
    with Session(engine) as session:
        session.execute(insert(Department).values([{"name": "QA"}, {"name": "Sales"}]))
        session.commit()


def batch_orm_insert():
    with Session(engine) as session:
        session.execute(
            insert(Employee).values(
                [
                    {
                        "department_id": select(Department.id).where(
                            Department.name == "hr"
                        ),
                        "name": "wwww",
                        "birthday": "2000-1-19",
                    },
                    {
                        "department_id": select(Department.id).where(
                            Department.name == "Sales"
                        ),
                        "name": "YYY",
                        "birthday": "2000-2-19",
                    },
                ]
            )
        )
        session.commit()


def batch_update():
    with Session(engine) as session:
        # 2种方式,第一种传入 id, 第二种使用 where 条件
        session.execute(
            update(Employee),
            [{"id": 2, "birthday": "1999-2-9"}, {"id": 5, "name": "Samuel"}],
        )

        session.execute(
            update(Employee).where(Employee.id == 4).values(name="Smith1"),
        )
        session.commit()


def batch_delete():
    with Session(engine) as session:
        session.execute(delete(Employee).where(Employee.name.in_(["wwww", "YYY"])))
        session.commit()


# batch_insert()
# batch_orm_insert()
# batch_update()
batch_delete()
