from db_init import Session, User, Role


def insert_records(session):
    existing_role1: Role = (
        session.query(Role).filter(Role.name == "Admin").one_or_none()
    )
    if existing_role1:
        role1 = existing_role1
    else:
        role1 = Role(name="Admin")
        session.add(role1)

    existing_role2 = session.query(Role).filter(Role.name == "Operator").one_or_none()
    if existing_role2:
        role2 = existing_role2
    else:
        role2 = Role(name="Operator")
        session.add(role2)

    user1 = User(name="Jack", password="111")
    user2 = User(name="Tom", password="222")
    user3 = User(name="Mary", password="333")

    # add roles to users
    user1.roles.append(role1)
    user1.roles.append(role2)

    user2.roles.append(role1)
    user3.roles.append(role2)

    session.add_all([user1, user2, user3])

    session.commit()


def select_user(session):
    user: User = session.query(User).filter(User.id == 1).one()
    print(user)
    print(user.roles)


# user: id: 1, name: Jack
# [role: id: 1, name: Admin,
#  role: id: 2, name: Operator]


def select_role(session):
    role: Role = session.query(Role).filter(Role.id == 2).one()
    print(role)
    print(role.users)


# role: id: 2, name: Operator
# [user: id: 1, name: Jack,
#  user: id: 3, name: Mary]


session = Session()

insert_records(session)
print("-" * 100)
select_user(session)
print("-" * 100)
select_role(session)
