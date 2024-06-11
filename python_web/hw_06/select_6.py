import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect("tables.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """SELECT s.student_name, g.group_name  FROM students s
JOIN groups g ON g.id = s.group_id 
WHERE s.group_id = 1
GROUP BY s.student_name 
ORDER BY s.student_name 
"""


print(execute_query(sql))
