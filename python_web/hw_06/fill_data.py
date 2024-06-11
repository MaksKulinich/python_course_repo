import sqlite3
from random import randint
import faker
from datetime import datetime

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 40
NUMBER_TEACHERS = 5
subjects = [
    "Mathematics",
    "Physics",
    "Chemistry",
    "Biology",
    "History",
    "Geography",
    "Literature",
]


def generate_data(number_groups, number_students, number_teachers):
    fake_groups = []
    fake_students = []
    fake_teachers = []

    fake_data = faker.Faker()

    for _ in range(number_groups):
        fake_groups.append(f"FIT-{randint(1, 10)}")

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    return fake_groups, fake_students, fake_teachers


def prepare_data(groups, students, teachers):
    for_groups = []

    for group in groups:
        for_groups.append((group,))

    for_students = []

    for student in students:
        for_students.append((student, randint(1, NUMBER_GROUPS)))

    for_teachers = []

    for teacher in teachers:
        for_teachers.append((teacher,))

    for_subjects = []

    for subject in subjects:
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))

    for_scores = []

    for month in range(1, 6):
        put_at = datetime(2023, month, randint(1, 28)).date()

        for student in students:
            for_scores.append(
                (randint(1, 5), put_at, randint(1, NUMBER_STUDENTS), randint(1, 7))
            )

    return for_groups, for_students, for_teachers, for_subjects, for_scores


def insert_data_to_db(groups, students, teachers, subjects, scores):
    with sqlite3.connect("tables.db") as con:
        cur = con.cursor()

        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""

        cur.executemany(sql_to_groups, groups)

        sql_to_students = """INSERT INTO students(student_name, group_id)
                               VALUES (?, ?)"""

        cur.executemany(sql_to_students, students)

        sql_to_teachers = """INSERT INTO teachers(teacher_name)
                               VALUES (?)"""

        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = """INSERT INTO subjects(subject_name, teacher_id)
                               VALUES (?, ?)"""

        cur.executemany(sql_to_subjects, subjects)

        sql_to_scores = """INSERT INTO scores(mark, created_at, student_id, subject_id)
                               VALUES (?, ?, ?, ?)"""

        cur.executemany(sql_to_scores, scores)

        con.commit()


if __name__ == "__main__":
    gr, st, teach, subj, scor = prepare_data(
        *generate_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_TEACHERS)
    )
    insert_data_to_db(gr, st, teach, subj, scor)
