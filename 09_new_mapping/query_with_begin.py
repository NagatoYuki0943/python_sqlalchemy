import time
from db_init import Session, Person


# session.begin() 异常时自动回滚
with Session.begin() as session:
    c = Person(name="Perfume", birthday="2000-10-1")

    session.add(c)

    session.commit()
    session.flush()

    time.sleep(5)

    session.query(Person).filter_by(name="Perfume").update({"birthday": "2000-10-2"})
    session.commit()


# 等价
# with Session() as session:
#     try:
#         # 操作
#         session.commit()
#     except:
#         session.rollback()
#         raise
