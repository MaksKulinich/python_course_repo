from datetime import datetime

from sqlalchemy import create_engine, Integer, String, Boolean
from sqlalchemy.orm import (
    relationship,
    sessionmaker,
    Mapped,
    mapped_column,
    declarative_base,
)
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime

engine = create_engine("sqlite:///mynotes.db", echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    group_name: Mapped[str] = mapped_column(String(50))


class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    student_name: Mapped[str] = mapped_column(String(100))
    group_id: Mapped[str] = mapped_column("group_id", Integer, ForeignKey("groups.id"))
    group: Mapped["Group"] = relationship(Group)


class Teacher(Base):
    __tablename__ = "teachers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    teacher_name: Mapped[str] = mapped_column(String(100))


class Subject(Base):
    __tablename__ = "subjects"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    subject_name: Mapped[str] = mapped_column(String(50))
    teacher_id: Mapped[int] = mapped_column(
        "teacher_id", Integer, ForeignKey("teachers.id")
    )
    teacher: Mapped["Teacher"] = relationship(Teacher)


class Score(Base):
    __tablename__ = "scores"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    mark: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[DateTime] = mapped_column(DateTime)
    student_id: Mapped[int] = mapped_column(
        "student_id", Integer, ForeignKey("students.id")
    )
    subject_id: Mapped[int] = mapped_column(
        "subject_id", Integer, ForeignKey("subjects.id")
    )
    student: Mapped[Student] = relationship(Student)
    subject: Mapped[Subject] = relationship(Subject)


Base.metadata.create_all(engine)
