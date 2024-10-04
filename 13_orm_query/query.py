from sqlalchemy import Select, select, insert, update, bindparam, delete
from sqlalchemy.orm import outerjoin, aliased

from db_init import Session, Department, Employee


def execute_query(query):
    # 通过 session.execute() 执行查询, 而不是 使用 session.query()
    # execute() 后面可以使用 all fetchall() 等方法获取结果
    result = session.execute(query).all()
    for row in result:
        print(row)


def select_single_target():
    query: Select = select(Department).order_by(Department.name)
    execute_query(query)


# (department: id: 1, name: hr,)
# (department: id: 2, name: it,)


def select_multiple():
    # 查询2个类, 使用 join, 并指定 isouter=True, 即使没有对应的数据也会返回空值
    # 下面2种写法是等价的
    query: Select = select(Employee, Department).join(Employee.department, isouter=True)
    query: Select = select(Employee, Department).join(
        Department.employees, isouter=True
    )
    execute_query(query)


# (employee: id: 1, department: department: id: 1, name: hr, name: Jack, birthday: 1990-01-01 12:00:00, department: id: 1, name: hr)
# (employee: id: 2, department: department: id: 1, name: hr, name: Tom, birthday: 1990-01-02 13:00:00, department: id: 1, name: hr)
# (employee: id: 3, department: department: id: 1, name: hr, name: Mary, birthday: 1990-01-03 14:00:00, department: id: 1, name: hr)
# (employee: id: 4, department: department: id: 2, name: it, name: Smith, birthday: 1990-01-04 09:00:00, department: id: 2, name: it)
# (employee: id: 5, department: department: id: 2, name: it, name: Rose, birthday: 1990-01-05 10:00:00, department: id: 2, name: it)
# (employee: id: 6, department: department: id: 2, name: it, name: Leon, birthday: 1990-01-06 18:00:00, department: id: 2, name: it)
# (employee: id: 18, department: department: id: 1, name: hr, name: Jerry, birthday: 2000-10-01 00:00:00, department: id: 1, name: hr)


# 添加别名
def select_with_alias():
    emp_cls = aliased(Employee, name="emp")
    dep_cls = aliased(Department, name="dep")
    # of_type: 指定 join 的类的别名
    query: Select = select(emp_cls, dep_cls).join(
        emp_cls.department.of_type(dep_cls), isouter=True
    )
    execute_query(query)


# SELECT emp.id, emp.department_id, emp.name, emp.birthday, dep.id AS id_1, dep.name AS name_1 FROM employee AS emp INNER JOIN department AS dep ON dep.id = emp.department_id
# (employee: id: 1, department: department: id: 1, name: hr, name: Jack, birthday: 1990-01-01 12:00:00, department: id: 1, name: hr)
# (employee: id: 2, department: department: id: 1, name: hr, name: Tom, birthday: 1990-01-02 13:00:00, department: id: 1, name: hr)
# (employee: id: 3, department: department: id: 1, name: hr, name: Mary, birthday: 1990-01-03 14:00:00, department: id: 1, name: hr)
# (employee: id: 4, department: department: id: 2, name: it, name: Smith, birthday: 1990-01-04 09:00:00, department: id: 2, name: it)
# (employee: id: 5, department: department: id: 2, name: it, name: Rose, birthday: 1990-01-05 10:00:00, department: id: 2, name: it)
# (employee: id: 6, department: department: id: 2, name: it, name: Leon, birthday: 1990-01-06 18:00:00, department: id: 2, name: it)
# (employee: id: 18, department: department: id: 1, name: hr, name: Jerry, birthday: 2000-10-01 00:00:00, department: id: 1, name: hr)


# 查询指定字段
def select_fields():
    # label: 为字段指定别名, 为了避免命名冲突
    # join_from: 指定 join 的类, 上面使用 join, 是因为上面 select 直接使用了类, 而这里 select 的是字段
    query: Select = select(
        Employee.name.label("emp_name"), Department.name.label("dep_name")
    ).join_from(Employee, Department, isouter=True)
    execute_query(query)


# SELECT employee.name AS emp_name, department.name AS dep_name FROM employee INNER JOIN department ON department.id = employee.department_id
# ('Jack', 'hr')
# ('Tom', 'hr')
# ('Mary', 'hr')
# ('Smith', 'it')
# ('Rose', 'it')
# ('Leon', 'it')
# ('Jerry', 'hr')


# outer join
def select_fields_outer():
    # select_from & outerjoin 等价于 join_from & isouter=True
    query: Select = select(
        Employee.name.label("emp_name"), Department.name.label("dep_name")
    ).select_from(outerjoin(Employee, Department))
    execute_query(query)


# SELECT employee.name AS emp_name, department.name AS dep_name FROM employee LEFT OUTER JOIN department ON department.id = employee.department_id
# ('Jack', 'hr')
# ('Tom', 'hr')
# ('Mary', 'hr')
# ('Smith', 'it')
# ('Rose', 'it')
# ('Leon', 'it')
# ('Jerry', 'hr')


# 条件判断直接使用对象
def where_obj():
    # get: 根据 id 获取对象
    dep = session.get(Department, 1)
    # 下面2种写法是等价的, 直接让 部门字段等于对象 或者 部门id等于对象id
    query = select(Employee).where(Employee.department == dep)
    # query: Select = select(Employee).where(Employee.department_id != dep.id)
    execute_query(query)


# (employee: id: 1, department: department: id: 1, name: hr, name: Jack, birthday: 1990-01-01 12:00:00,)
# (employee: id: 2, department: department: id: 1, name: hr, name: Tom, birthday: 1990-01-02 13:00:00,)
# (employee: id: 3, department: department: id: 1, name: hr, name: Mary, birthday: 1990-01-03 14:00:00,)
# (employee: id: 18, department: department: id: 1, name: hr, name: Jerry, birthday: 2000-10-01 00:00:00,)


# contains, 得到员工, 查询部门信息, 不常使用
def select_contains():
    # get: 根据 id 获取对象
    emp = session.get(Employee, 1)
    query: Select = select(Department).where(Department.employees.contains(emp))
    query: Select = select(Department).where(Department.id == emp.department_id)
    execute_query(query)


# (department: id: 1, name: hr,)


session = Session()

select_single_target()
print("=" * 100)
select_multiple()
print("=" * 100)
select_with_alias()
print("=" * 100)
select_fields()
print("=" * 100)
select_fields_outer()
print("=" * 100)
where_obj()
print("=" * 100)
select_contains()
