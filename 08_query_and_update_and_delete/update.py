from db_init import Session, Person


session = Session()


# 修改单条记录
person = session.query(Person).filter(Person.id == 1).one()
# 修改字段值
person.address = "wwww"
session.commit()


# 修改单条记录
# 使用 update() 方法
session.query(Person).filter(Person.id == 2).update({Person.address: "PPPP"})
session.commit()


# 修改多条记录
session.query(Person).filter(Person.id > 8).update({Person.address: "Beijing"})
session.commit()
