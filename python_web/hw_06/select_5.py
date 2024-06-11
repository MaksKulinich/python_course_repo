import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect("tables.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """SELECT t.teacher_name, s.subject_name  FROM teachers t 
JOIN subjects s ON s.teacher_id = t.id  
WHERE t.id = 1
GROUP BY s.subject_name 
ORDER BY t.teacher_name ASC 
"""


print(execute_query(sql))
