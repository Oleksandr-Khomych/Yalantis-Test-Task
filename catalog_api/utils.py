import datetime
from flask_restful import abort
from db_methods import course_exists


def transfer_date(raw_date: str) -> datetime.date:
    """
    Example:
    "2021-04-20" => datetime(year=2021, month=04, day=20)
    :param raw_date: str
    :return: datetime.date
    """
    date_obj = datetime.datetime.strptime(raw_date, '%Y-%m-%d').date()
    return date_obj


def validate_lectures_count(value, name):
    try:
        value = int(value)
    except ValueError:
        raise ValueError(f"The parameter '{name}' is not int. You gave us the value type: {type(value)}")
    if value < 1:
        raise ValueError(f"The parameter '{name}' can`t be less than 1. You give the value: {value}")
    return value


def abort_if_course_doesnt_exist(course_id):
    if not course_exists(course_id):
        abort(404, message=f"Course {course_id} doesn't exist!")
