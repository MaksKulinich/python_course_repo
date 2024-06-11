import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect("tables.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """SELECT ROUND(AVG(sc.mark), 2), g.group_name  FROM scores sc
JOIN groups g, students s  ON g.id = s.group_id and sc.student_id = s.id 
WHERE sc.subject_id = 4
GROUP BY g.group_name 
ORDER BY AVG(SC.mark) DESC 
"""


print(execute_query(sql))
