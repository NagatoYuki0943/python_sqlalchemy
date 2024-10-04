from db_init import Session, Person
from sqlalchemy.sql import between


session = Session()


rows = session.query(Person).filter(Person.id.in_([1, 2, 3]))
for person in rows:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)
# id: 1, name: Tom, birthday: 2000-10-11
# id: 2, name: Jack, birthday: 2000-10-13
# id: 3, name: Mary, birthday: 2000-10-14


rows = session.query(Person).filter(Person.id.between(1, 3))
for person in rows:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)
# id: 1, name: Tom, birthday: 2000-10-11
# id: 2, name: Jack, birthday: 2000-10-13
# id: 3, name: Mary, birthday: 2000-10-14


rows = session.query(Person).filter(between(Person.id, 1, 3))
for person in rows:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)
# id: 1, name: Tom, birthday: 2000-10-11
# id: 2, name: Jack, birthday: 2000-10-13
# id: 3, name: Mary, birthday: 2000-10-14
