import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect("tables.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """SELECT ROUND(AVG(sc.mark), 2) FROM scores sc"""


print(execute_query(sql))
