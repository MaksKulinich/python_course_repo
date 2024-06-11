import sqlite3


def create_database():
    with open("tables.sql", "r") as file:
        data_file = file.read()

    with sqlite3.connect("tables.db") as con:
        cur = con.cursor()
        cur.executescript(data_file)


if __name__ == "__main__":
    create_database()
