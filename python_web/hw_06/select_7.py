import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect("tables.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.student_name, sc.mark
FROM scores sc
JOIN students s ON sc.student_id = s.id
WHERE sc.subject_id = 1
AND s.group_id = 2;
"""

print(execute_query(sql))
