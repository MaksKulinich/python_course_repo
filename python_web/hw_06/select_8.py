import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect("tables.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """SELECT AVG(sc.mark) FROM scores sc
JOIN subjects sub ON sc.subject_id = sub.id
WHERE sub.teacher_id = 2;
"""

print(execute_query(sql))
