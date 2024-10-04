from db_init import engine, department, employee
import sqlalchemy


join = employee.join(department, employee.c.department_id == department.c.id)


with engine.connect() as conn:
    # 查询员工和部门
    # select(join): 两张表join后的一张大表
    query = sqlalchemy.select(join).where(department.c.name == "hr")
    print(conn.execute(query).all())
print("=" * 100)
# [(1, 1, 'Jack', datetime.datetime(1990, 1, 1, 12, 0), 1, 'hr'), (2, 1, 'Tom', datetime.datetime(1990, 1, 2, 13, 0), 1, 'hr'), (3, 1, 'Mary', datetime.datetime(1990, 1, 3, 14, 0), 1, 'hr')]


with engine.connect() as conn:
    # 查询员工
    # select(employee): 指定查询要返回的列或表达式, 查询员工表
    # select_from(join): 显式指定查询的FROM子句, 即join后的结果
    query = (
        sqlalchemy.select(employee).select_from(join).where(department.c.name == "hr")
    )
    print(conn.execute(query).all())
print("=" * 100)
# [(1, 1, 'Jack', datetime.datetime(1990, 1, 1, 12, 0)), (2, 1, 'Tom', datetime.datetime(1990, 1, 2, 13, 0)), (3, 1, 'Mary', datetime.datetime(1990, 1, 3, 14, 0))]


with engine.connect() as conn:
    # 查询部门
    # select(department): 指定查询要返回的列或表达式, 查询部门表
    # select_from(join): 显式指定查询的FROM子句, 即join后的结果
    query = (
        sqlalchemy.select(department).select_from(join).where(employee.c.name == "Rose")
    )
    print(conn.execute(query).all())
print("=" * 100)
# [(2, 'it')]
