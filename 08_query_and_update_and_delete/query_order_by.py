from db_init import Session, Person


session = Session()


# order_by() 排序, 默认升序, 可以手动指定排序方向
rows = session.query(Person).order_by(Person.id.asc())
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


# order_by() 排序, 默认升序, 可以手动指定排序方向
rows = session.query(Person).order_by(Person.birthday.desc(), Person.id)
for person in rows:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)
# id: 6, name: Jerry, birthday: 2000-10-17
# id: 5, name: Luck, birthday: 2000-10-16
# id: 4, name: Smith, birthday: 2000-10-15
# id: 3, name: Mary, birthday: 2000-10-14
# id: 2, name: Jack, birthday: 2000-10-13
# id: 1, name: Tom, birthday: 2000-10-11
# id: 8, name: Amy, birthday: 2000-09-18
# id: 9, name: Eric, birthday: 1998-02-18
# id: 10, name: Samuel, birthday: 1997-01-15
