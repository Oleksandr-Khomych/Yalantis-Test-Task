from datetime import date

from app import db
from models import Course


def add_course(name: str, start_date: date, end_date: date, lectures_count: int) -> int:
    new_course = Course(name=name, start_date=start_date, end_date=end_date, lectures_count=lectures_count)
    db.session.add(new_course)
    db.session.commit()
    return new_course.id
