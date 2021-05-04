from datetime import date

from catalog_api.app import db
from catalog_api.models import Course


def add_course(name: str, start_date: date, end_date: date, lectures_count: int) -> int:
    new_course = Course(name=name, start_date=start_date, end_date=end_date, lectures_count=lectures_count)
    db.session.add(new_course)
    db.session.commit()
    return new_course.id


def get_all_course():
    return db.session.query(Course).all()


def get_course_by_id(id_: int):
    return db.session.query(Course).filter(Course.id == id_).first()


def course_exists(id_: int) -> bool:
    return bool(db.session.query(Course).filter(Course.id == id_).count())


def delete_course_by_id(id_: int):
    db.session.query(Course).filter(Course.id == id_).delete()
    db.session.commit()


def update_course_info(id_: int, update_data: dict):
    db.session.query(Course).filter(Course.id == id_).update(update_data)
    db.session.commit()


def find_courses(filters: dict):
    q = db.session.query(Course).filter(Course.name.like(f'%{filters["name"]}%'))
    if filters['start_date[gte]']:
        q = q.filter(Course.start_date >= filters['start_date[gte]'])
    if filters['start_date[lte]']:
        q = q.filter(Course.start_date <= filters['start_date[lte]'])

    if filters['end_date[gte]']:
        q = q.filter(Course.end_date >= filters['end_date[gte]'])
    if filters['end_date[lte]']:
        q = q.filter(Course.end_date <= filters['end_date[lte]'])
    return q.all()
