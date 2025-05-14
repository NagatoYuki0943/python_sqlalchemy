import time
from db_init import Session, Person


session = Session()

c = Person(name="Perfume", birthday="2000-10-1")

session.add(c)

session.commit()
session.flush()

time.sleep(5)

session.query(Person).filter_by(name="Perfume").update({"birthday": "2000-10-2"})
session.commit()
