from sqlalchemy import select, func, desc, and_
from sqlalchemy.orm import sessionmaker
from models import Group, Student, Teacher, Subject, Score, engine


Session = sessionmaker(bind=engine)
session = Session()


def select_1() -> list:
    stmt = (
        select(
            Student.student_name, func.round(func.avg(Score.mark), 2).label("avg_grade")
        )
        .select_from(Score)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
    )

    results = session.execute(stmt).all()

    return results


def select_2(subj_id: int) -> list:
    stmt = (
        select(
            Student.student_name,
            func.round(func.avg(Score.mark), 2).label("avg_grade"),
        )
        .select_from(Student)
        .join(Score, Score.student_id == Student.id)
        .where(Score.subject_id == subj_id)
        .group_by(Student.student_name)
        .order_by(desc("avg_grade"))
        .limit(1)
    )

    result = session.execute(stmt).all()

    return result


def select_3(subj_id):
    stmt = (
        select(func.round(func.avg(Score.mark), 2).label("avg_grade"), Group.group_name)
        .select_from(Score)
        .join(Group, Group.id == Student.group_id)
        .join(Student, Score.student_id == Student.id)
        .where(Score.subject_id == subj_id)
        .group_by(Group.group_name)
        .order_by(desc("avg_grade"))
    )
    result = session.execute(stmt).all()

    return result


def select_4():
    stmt = select(func.round(func.avg(Score.mark), 2)).select_from(Score)

    result = session.execute(stmt).scalar()

    return result


def select_5(teach_id: int) -> list:
    stmt = (
        select(Teacher.teacher_name, Subject.subject_name)
        .select_from(Teacher)
        .join(Subject, Subject.teacher_id == Teacher.id)
        .where(Teacher.id == teach_id)
        .group_by(Subject.subject_name)
    )

    result = session.execute(stmt).all()

    return result


def select_6(gr_id):
    stmt = (
        select(Student.student_name, Group.group_name)
        .select_from(Student)
        .join(Group, Student.group_id == Group.id)
        .where(Group.id == gr_id)
        .group_by(Student.student_name)
        .order_by(Student.student_name)
    )

    result = session.execute(stmt).all()

    return result


def select_7(subj_id, gr_id):
    stmt = (
        select(Score.mark, Student.student_name)
        .select_from(Score)
        .join(Student, Score.student_id == Student.id)
        .where(and_(Score.subject_id == subj_id, Student.group_id == gr_id))
    )

    result = session.execute(stmt).all()

    return result


def select_8(teach_id):
    stmt = (
        select(func.avg(Score.mark))
        .select_from(Score)
        .join(Subject, Score.subject_id == Subject.id)
        .where(Subject.teacher_id == teach_id)
    )

    result = session.execute(stmt).scalar()

    return result


def select_9(stud_id):
    stmt = (
        select(Subject.id, Subject.subject_name)
        .select_from(Score)
        .join(Subject, Score.subject_id == Subject.id)
        .where(Score.student_id == stud_id)
        .group_by(Subject.subject_name)
        .order_by(Subject.id)
    )

    result = session.execute(stmt).all()

    return result


def select_10(stud_id, teach_id):
    stmt = (
        select(Subject.subject_name, Subject.id)
        .select_from(Score)
        .join(Subject, Score.subject_id == Subject.id)
        .where(and_(Subject.teacher_id == teach_id, Score.student_id == stud_id))
        .group_by(Subject.subject_name)
        .order_by(Subject.id)
    )

    result = session.execute(stmt).all()

    return result


if __name__ == "__main__":
    print(select_10(2, 4))
