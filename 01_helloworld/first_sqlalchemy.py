# pip install sqlalchemy mysqlclient
import sqlalchemy
from sqlalchemy import Engine, Connection, TextClause, CursorResult, Row

# mysql://username:password@hostname:port/database_name
# echo=True: 显示执行的SQL语句
engine: Engine = sqlalchemy.create_engine(
    "mysql://root:root@localhost:3306/mb", echo=True
)

# create a connection
conn: Connection = engine.connect()

# create a query
query: TextClause = sqlalchemy.text("SELECT * FROM students1")

# execute the query and get the result set
result_set: CursorResult = conn.execute(query)

# iterate over the result set and print each row
row: Row
for row in result_set:
    print(row)

# close the connection
conn.close()

# dispose the engine
engine.dispose()
