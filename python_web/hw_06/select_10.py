import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect("tables.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """SELECT sub.id AS subject_id, sub.subject_name
FROM scores sc
JOIN subjects sub ON sc.subject_id = sub.id
WHERE sc.student_id = 1
AND sub.teacher_id = 2
GROUP BY sub.id, sub.subject_name;
"""

print(execute_query(sql))
