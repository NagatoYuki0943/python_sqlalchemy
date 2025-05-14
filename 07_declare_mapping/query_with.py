from db_init import Session, Person


# with Session() as session: 语法会在代码块结束时自动调用 session.close()，无论是否发生异常。
with Session() as session:
    # 添加一条数据
    p = Person(name="Amy", birthday="2000-9-18", address="unknown")
    session.add(p)
    # 提交
    session.commit()

    # 添加多条数据
    person_list = [
        Person(name="Eric", birthday="1998-2-18", address="unknown"),
        Person(name="Samuel", birthday="1997-1-15", address="unknown"),
    ]
    session.add_all(person_list)
