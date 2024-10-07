# pip install sqlalchemy
# pip install mysqlclient (for mysql)
# pip install psycopg2 (for postgres)
import sqlalchemy
from sqlalchemy import Engine, Connection, TextClause, CursorResult, Row


# database://username:password@hostname:port/database_name
database_type = "postgresql"
if database_type == "mysql":
    url = "mysql://root:root@localhost:3306/mb"
elif database_type == "postgresql":
    url = "postgresql://postgres:postgres@localhost:5432/mb"
else:
    raise ValueError("Unsupported database type")

# echo=True: 显示执行的SQL语句
engine: Engine = sqlalchemy.create_engine(url, echo=True)

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
