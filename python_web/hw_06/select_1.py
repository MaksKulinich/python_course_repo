import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect("tables.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """SELECT s.student_name, ROUND(AVG(sc.mark), 2) FROM students s
JOIN scores sc ON s.id = sc.student_id
GROUP BY s.student_name 
ORDER BY AVG(sc.mark) DESC 
LIMIT 5
"""

print(execute_query(sql))
