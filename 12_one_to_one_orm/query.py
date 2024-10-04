from db_init import Session, Employee, Computer


def insert(session):
    existing_computer1 = (
        session.query(Computer).filter(Computer.model == "Dell").one_or_none()
    )
    if existing_computer1:
        computer1 = existing_computer1
    else:
        computer1 = Computer(model="Dell", number="1111")
        session.add(computer1)

    existing_computer2 = (
        session.query(Computer).filter(Computer.model == "Surface").one_or_none()
    )
    if existing_computer2:
        computer2 = existing_computer2
    else:
        computer2 = Computer(model="Surface", number="2222")
        session.add(computer2)

    existing_computer3 = (
        session.query(Computer).filter(Computer.model == "MacBook Pro").one_or_none()
    )
    if existing_computer3:
        existing_computer3 = existing_computer3
    else:
        computer3 = Computer(model="MacBook Pro", number="3333")
        session.add(computer3)

    employee1 = Employee(name="Name1", computer=computer1)
    employee2 = Employee(name="Name2", computer=computer2)
    employee3 = Employee(name="Name3", computer=computer3)

    session.add_all([employee1, employee2, employee3])

    session.commit()


def select(session):
    employee: Employee = session.query(Employee).filter(Employee.id == 1).one_or_none()
    if employee:
        print(employee)
        print(employee.computer)

    computer: Computer = session.query(Computer).filter(Computer.id == 2).one_or_none()
    if computer:
        print(computer)
        print(computer.employee)


# employee: id: 1, name: Name1
# computer: id: 1, model: Dell, number: 1111
# computer: id: 2, model: Surface, number: 2222
# employee: id: 2, name: Name2


def update_1(session):
    row: Employee = session.query(Employee).filter(Employee.id == 2).one_or_none()
    print(row)
    print(row.computer)

    session.query(Employee).filter(Employee.id == 2).update(
        {Employee.computer_id: None}
    )
    session.commit()

    row: Employee = session.query(Employee).filter(Employee.id == 2).one_or_none()
    print(row)
    print(row.computer)


# employee: id: 2, name: Name2
# computer: id: 2, model: Surface, number: 2222
# employee: id: 2, name: Name2
# None


def update_2(session):
    row: Employee = session.query(Employee).filter(Employee.id == 3).one_or_none()
    print(row)
    print(row.computer)

    computer: Computer = session.query(Computer).filter(Computer.id == 3).one_or_none()
    employee: Employee = session.query(Employee).filter(Employee.id == 3).one_or_none()
    if computer and employee:
        employee.computer = computer
        session.commit()

    row: Employee = session.query(Employee).filter(Employee.id == 3).one_or_none()
    print(row)
    print(row.computer)


# employee: id: 3, name: Name3
# computer: id: 3, model: MacBook Pro, number: 3333
# employee: id: 3, name: Name3
# computer: id: 3, model: MacBook Pro, number: 3333


session = Session()
insert(session)
print("-" * 100)
select(session)
print("-" * 100)
update_1(session)
print("-" * 100)
update_2(session)
