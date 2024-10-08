from db_init import Session, Person
from sqlalchemy.sql import and_, or_


session = Session()


# query(目标类)
rows = session.query(Person).all()
for person in rows:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)
# id: 1, name: Tom, birthday: 2000-10-11
# id: 2, name: Jack, birthday: 2000-10-13
# id: 3, name: Mary, birthday: 2000-10-14
# id: 4, name: Smith, birthday: 2000-10-15
# id: 5, name: Luck, birthday: 2000-10-16
# id: 6, name: Jerry, birthday: 2000-10-17
# id: 8, name: Amy, birthday: 2000-09-18
# id: 9, name: Eric, birthday: 1998-02-18
# id: 10, name: Samuel, birthday: 1997-01-15


# 最后不写 all() 也可以得到结果
# filter() == where()
rows = session.query(Person).filter(Person.address == "aaa")
for person in rows:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)
# id: 4, name: Smith, birthday: 2000-10-15


# 多个 filter 条件默认使用 and_ 连接
rows = (
    session.query(Person).filter(Person.id > 3).filter(Person.birthday < "2000-10-15")
)
for person in rows:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)
# id: 8, name: Amy, birthday: 2000-09-18
# id: 9, name: Eric, birthday: 1998-02-18
# id: 10, name: Samuel, birthday: 1997-01-15


# 多个 filter 条件默认使用 and_ 连接
rows = session.query(Person).filter(Person.id > 3, Person.birthday < "2000-10-15")
for person in rows:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)
# id: 8, name: Amy, birthday: 2000-09-18
# id: 9, name: Eric, birthday: 1998-02-18
# id: 10, name: Samuel, birthday: 1997-01-15


rows = session.query(Person).filter(and_(Person.id > 3, Person.birthday < "2000-10-15"))
for person in rows:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)
# id: 8, name: Amy, birthday: 2000-09-18
# id: 9, name: Eric, birthday: 1998-02-18
# id: 10, name: Samuel, birthday: 1997-01-15


rows = session.query(Person).filter(
    or_(
        Person.name == "Tom",
        and_(Person.birthday > "2000-10-13", Person.id < 5),
    )
)
for person in rows:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)
# id: 1, name: Tom, birthday: 2000-10-11
# id: 3, name: Mary, birthday: 2000-10-14
# id: 4, name: Smith, birthday: 2000-10-15


# 值不存在不会报错
rows = session.query(Person).filter(Person.id > 100)
for person in rows:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)


# filter_by(), 直接填写属性名和值, 支持多个条件
rows = session.query(Person).filter_by(name="Tom")
for person in rows:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)
# id: 1, name: Tom, birthday: 2000-10-11
