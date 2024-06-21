from connect_db import session
from faker import Faker
import random

from models import Group, Student, Teacher, Subject, Score, engine


faker = Faker()


def create_groups(n):
    groups = []
    for _ in range(n):
        group = Group(group_name=faker.word())
        groups.append(group)
        session.add(group)
    session.commit()
    return groups


def create_students(n, groups):
    students = []
    for _ in range(n):
        student = Student(student_name=faker.name(), group_id=random.choice(groups).id)
        students.append(student)
        session.add(student)
    session.commit()
    return students


def create_teachers(n):
    teachers = []
    for _ in range(n):
        teacher = Teacher(teacher_name=faker.name())
        teachers.append(teacher)
        session.add(teacher)
    session.commit()
    return teachers


def create_subjects(n, teachers):
    subjects = []
    for _ in range(n):
        subject = Subject(
            subject_name=faker.word(), teacher_id=random.choice(teachers).id
        )
        subjects.append(subject)
        session.add(subject)
    session.commit()
    return subjects


def create_scores(students, subjects):
    for student in students:
        for subject in subjects:
            for _ in range(random.randint(1, 20)):
                score = Score(
                    mark=random.randint(1, 100),
                    created_at=faker.date_time_this_year(),
                    student_id=student.id,
                    subject_id=subject.id,
                )
                session.add(score)
    session.commit()


# Генерація даних
groups = create_groups(3)
students = create_students(30, groups)
teachers = create_teachers(5)
subjects = create_subjects(8, teachers)
create_scores(students, subjects)
