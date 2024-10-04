from db_init import Session, Person


session = Session()


# offset() limit() 分页
rows = session.query(Person).offset(2).limit(3)
for person in rows:
    print(f"id: {person.id}, name: {person.name}, birthday: {person.birthday}")
print("-" * 100)
# id: 3, name: Mary, birthday: 2000-10-14
# id: 4, name: Smith, birthday: 2000-10-15
# id: 5, name: Luck, birthday: 2000-10-16
