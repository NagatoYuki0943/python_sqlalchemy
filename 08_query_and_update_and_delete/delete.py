from db_init import Session, Person


session = Session()


# 当删除的对象不存在时，sqlalchemy不会抛出异常
session.query(Person).filter(Person.id == 11).delete()
session.commit()
