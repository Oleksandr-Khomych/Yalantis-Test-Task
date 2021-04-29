from flask_restful import Resource, reqparse

import db_methods
from app import app
from utils import transfer_date


@app.route('/')
def home():
    return '<h1>Home page!</h1>'


class CreateCourse(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('start_date', type=str,
                            help='The date must be in the format: "%Y-%m-%d"\n Example: "2021-04-20"')
        parser.add_argument('end_date', type=str,
                            help='The date must be in the format: "%Y-%m-%d"\n Example: "2021-04-20"')
        parser.add_argument('lectures_count', type=int, required=True)
        args = parser.parse_args(strict=True)
        name = args['name']
        lectures_count = args['lectures_count']

        try:
            start_date = transfer_date(args['start_date'])
        except ValueError as e:
            return {"message": {
                "start_date": f'{e}\nThe date must be in the format: "%Y-%m-%d"\n Example: "2021-04-20"'}}, 400
        try:
            end_date = transfer_date(args['end_date'])
        except ValueError as e:
            return {"message": {
                "end_date": f'{e}\nThe date must be in the format: "%Y-%m-%d"\n Example: "2021-04-20"'}}, 400

        id_ = db_methods.add_course(name, start_date, end_date, lectures_count)
        return {"message": {'id': id_, 'name': name, 'start_date': str(start_date), 'end_date': str(end_date)}}, 201


class Catalog(Resource):
    def get(self):
        courses = db_methods.get_all_course()
        courses_list = []
        for course in courses:
            courses_list.append({'id': course.id, 'name': course.name, 'lectures_count': course.lectures_count})
        return {"message": {"courses": courses_list}}, 200


class Course(Resource):
    def get(self, course_id):
        course = db_methods.get_course_by_id(course_id)
        if course:
            course_info = {'id': course.id, 'name': course.name, 'start_date': str(course.start_date),
                           'end_date': str(course.end_date), 'lectures_count': course.lectures_count}
            return {"message": {"course": course_info}}, 200
        else:
            return {"message": {"course": f"Course with id={course_id} not found"}}, 400

    def delete(self, course_id):
        if db_methods.course_exists(course_id):
            db_methods.delete_course_by_id(course_id)
            return {"message": {"delete": f"Course with id={course_id} successfully deleted!"}}, 200
        else:
            return {"message": {"delete": f"Course with id={course_id} not found!"}}, 400

    def patch(self, course_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('start_date', type=str,
                            help='The date must be in the format: "%Y-%m-%d"\n Example: "2021-04-20"')
        parser.add_argument('end_date', type=str,
                            help='The date must be in the format: "%Y-%m-%d"\n Example: "2021-04-20"')
        parser.add_argument('lectures_count', type=int)
        args = parser.parse_args(strict=True)
        update_data = {}
        if args['name']:
            update_data['name'] = args['name']
        if args['lectures_count']:
            update_data['lectures_count'] = args['lectures_count']

        if args['start_date']:
            try:
                start_date = transfer_date(args['start_date'])
                update_data['start_date'] = start_date
            except ValueError as e:
                return {"message": {
                    "start_date": f'{e}\nThe date must be in the format: "%Y-%m-%d"\n Example: "2021-04-20"'}}, 400
        if args['end_date']:
            try:
                end_date = transfer_date(args['end_date'])
                update_data['end_date'] = end_date
            except ValueError as e:
                return {"message": {
                    "end_date": f'{e}\nThe date must be in the format: "%Y-%m-%d"\n Example: "2021-04-20"'}}, 400
        db_methods.update_course_info(course_id, update_data)
        course = db_methods.get_course_by_id(course_id)
        course_info = {'id': course.id, 'name': course.name, 'start_date': str(course.start_date),
                       'end_date': str(course.end_date), 'lectures_count': course.lectures_count}
        return {"message": {"course": course_info}}, 200
