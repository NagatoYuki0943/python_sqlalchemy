from db_init import Session, Person
from sqlalchemy.orm import load_only


session = Session()


# first() 返回第一条记录(结果集中可能有多条记录)
person = session.query(Person).first()
if person:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)
# id: 1, name: Tom, birthday: 2000-10-11


# first() 没有值不会报错
person = session.query(Person).filter(Person.id == 100).first()
if person:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)


# one() 返回一条记录, 找到多条数据或者不存在的值会报错
person = session.query(Person).filter(Person.id == 1).one()
if person:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)
# id: 1, name: Tom, birthday: 2000-10-11


# one_or_none() 找到多条数据会报错, 不存在的值返回 None
person = session.query(Person).filter(Person.id == 1).one_or_none()
if person:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)
# id: 1, name: Tom, birthday: 2000-10-11


# one_or_none() 没有找到记录不会报错
person = session.query(Person).filter(Person.id == 100).one_or_none()
if person:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)


# scalar() 效果和 one_or_none() 类似, 找到多条数据会报错, 不存在的值返回 None
person = session.query(Person).filter(Person.id == 1).scalar()
if person:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)
# id: 1, name: Tom, birthday: 2000-10-11


# scalar() 没有找到记录不会报错
person = session.query(Person).filter(Person.id == 100).scalar()
if person:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)


# query 加载指定的字段
person = session.query(Person.name, Person.birthday).filter(Person.id == 1).first()
if person:
    print(f"name: {person.name}, birthday: {person.birthday}")
print("-" * 100)
# name: Tom, birthday: 2000-10-11
