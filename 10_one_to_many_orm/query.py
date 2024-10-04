from db_init import Session, Department, Employee


def insert_records(session):
    # Check if the department already exists
    existing_dept: Department = (
        session.query(Department).filter_by(name="hr").one_or_none()
    )
    if existing_dept:
        d1 = existing_dept
    else:
        d1 = Department(name="hr")
        # 这一行可以省略, 添加 Employee 时会自动添加 department
        session.add(d1)

    # 不传入 dep_id, 而是通过 department 字段来设置外键
    e1 = Employee(department=d1, name="Jerry", birthday="2000-10-1")
    session.add(e1)
    session.commit()


def select_employee(session):
    emp: Employee = session.query(Employee).filter(Employee.id == 1).one()

    print(emp)
    print(emp.department)


# department: id: 1, department_id: 1, name: Jack, birthday: 1990-01-01 12:00:00
# employee: id: 1, name: hr


def select_department(session):
    dep: Department = session.query(Department).filter(Department.id == 1).one()

    print(dep)
    print(dep.employees)


# employee: id: 1, name: hr
# [department: id: 1, department_id: 1, name: Jack, birthday: 1990-01-01 12:00:00,
#  department: id: 2, department_id: 1, name: Tom, birthday: 1990-01-02 13:00:00,
#  department: id: 3, department_id: 1, name: Mary, birthday: 1990-01-03 14:00:00,
#  department: id: 15, department_id: 1, name: Jerry, birthday: 2000-10-01 00:00:00]


session = Session()

insert_records(session)
print("-" * 100)
select_employee(session)
print("-" * 100)
select_department(session)
