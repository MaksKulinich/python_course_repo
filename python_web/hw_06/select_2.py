import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect("tables.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """SELECT st.student_name, ROUND(AVG(sc.mark), 2)  FROM students st 
JOIN scores sc ON sc.student_id = st.id 
WHERE sc.subject_id = 5
GROUP BY st.student_name 
ORDER BY AVG(sc.mark) DESC
LIMIT 1
"""


print(execute_query(sql))
